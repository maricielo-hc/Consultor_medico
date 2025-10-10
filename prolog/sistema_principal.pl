:- set_prolog_flag(encoding, utf8).
:- dynamic registro_sintoma/3.

% ====== CARGAR ARCHIVO DE REGLAS EXISTENTE ======
:- (exists_file('prolog/base_conocimiento.pl') ->
        consult('prolog/base_conocimiento.pl');
        write('No se encontró el archivo de reglas. Se creará uno nuevo.'), nl,
        open('prolog/base_conocimiento.pl', write, Stream),
        close(Stream)
   ).

% =========================================
% ========== MODO PACIENTE =================
% =========================================
modo_paciente :-
    write('--- Modo Paciente ---'), nl,
    write('Por favor, ingrese su nombre (entre comillas, por ejemplo "mari"): '),
    read(Usuario),
    diagnosticar_enfermedad(Usuario),
    mostrar_registros_usuario(Usuario).

diagnosticar_enfermedad(Usuario) :-
    write('Ingrese un síntoma (o "fin" para terminar): '),
    read(Sintoma),
    (   Sintoma == fin ->
        write('Fin del ingreso de síntomas.'), nl,
        sugerir_diagnostico(Usuario)
    ;   write('¿Cuántos días lleva con '), write(Sintoma), write('?: '),
        read(Dias),
        assertz(registro_sintoma(Usuario, Sintoma, Dias)),
        diagnosticar_enfermedad(Usuario)
    ).

mostrar_registros_usuario(Usuario) :-
    nl, write('--- Resumen de síntomas registrados para '),
    write(Usuario), write(' ---'), nl,
    forall(registro_sintoma(Usuario, S, D),
           (write('Síntoma: '), write(S),
            write(' | Duración: '), write(D), write(' días'), nl)).

sugerir_diagnostico(Usuario) :-
    (   posible_enfermedad(Usuario, Enfermedad) ->
        nl, write('Posible diagnóstico para '), write(Usuario), write(': '),
        write(Enfermedad), nl, nl
    ;   write('No se pudo determinar una enfermedad con los síntomas registrados.'), nl
    ).

tiene_sintoma(Usuario, Sintoma, MinDias) :-
    registro_sintoma(Usuario, Sintoma, D),
    D >= MinDias.

% =========================================
% ========== MODO DOCTOR ==================
% =========================================
modo_doctor :-
    write('--- Modo Doctor ---'), nl,
    write('Ingrese el nombre de la nueva enfermedad (por ejemplo: gripe_estacional): '),
    read(Enfermedad),
    write('Ingrese los síntomas requeridos (una lista entre corchetes, ej: [fiebre, tos]): '),
    read(ListaSintomas),
    write('Ingrese el número mínimo de días que debe durar cada síntoma (ej: 2): '),
    read(MinDias),
    agregar_regla(Enfermedad, ListaSintomas, MinDias),
    write('Regla agregada exitosamente.'), nl.

agregar_regla(Enfermedad, ListaSintomas, MinDias) :-
    open('reglas_enfermedades.pl', append, Stream),
    write(Stream, 'posible_enfermedad(U, '), write(Stream, Enfermedad), write(Stream, ') :-'), nl(Stream),
    escribir_sintomas(Stream, ListaSintomas, MinDias),
    write(Stream, '    true.'), nl(Stream), nl(Stream),
    close(Stream),
    consult('reglas_enfermedades.pl').

escribir_sintomas(_, [], _).
escribir_sintomas(Stream, [S|Resto], MinDias) :-
    write(Stream, '    tiene_sintoma(U, '), write(Stream, S), write(Stream, ', '), write(Stream, MinDias), write(Stream, '),'), nl(Stream),
    escribir_sintomas(Stream, Resto, MinDias).

% =========================================
% ========== MENÚ PRINCIPAL ===============
% =========================================
iniciar_sistema_experto :-
    write('Bienvenido al sistema experto de diagnóstico de enfermedades.'), nl,
    write('Seleccione su rol (paciente o doctor): '),
    read(Rol),
    (   Rol == paciente -> modo_paciente
    ;   Rol == doctor -> modo_doctor
    ;   write('Rol no válido. Intente nuevamente.'), nl, iniciar_sistema_experto
    ).

