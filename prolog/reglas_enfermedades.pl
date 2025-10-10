% ============================
% Base de conocimiento ampliada
% Sistema Experto de Síntomas (versión con duración)
% ============================

% ------------------------------------
% Declaración dinámica de síntomas
% ------------------------------------
:- dynamic registro_sintoma/3.

% ------------------------------------
% Reglas principales de diagnóstico
% ------------------------------------
% Reglas que combinan síntomas y duración (por usuario)

posible_enfermedad(U, gripe) :-
    tiene_sintoma(U, fiebre, 1),
    tiene_sintoma(U, dolor_cabeza, 1),
    tiene_sintoma(U, tos, 1),
    tiene_sintoma(U, dolor_muscular, 1),
    \+ fiebre_prolongada(U).

posible_enfermedad(U, neumonia) :-
    fiebre_prolongada(U),
    tiene_sintoma(U, tos, 3),
    tiene_sintoma(U, dificultad_respiratoria, 3).

posible_enfermedad(U, covid) :-
    tiene_sintoma(U, fiebre, 2),
    tiene_sintoma(U, dolor_muscular, 2),
    tiene_sintoma(U, anosmia, 1).

posible_enfermedad(U, apendicitis) :-
    tiene_sintoma(U, dolor_abdominal, 1),
    tiene_sintoma(U, vomito, 1),
    tiene_sintoma(U, dolor_hipocondrio_derecho, 1).

posible_enfermedad(U, meningitis) :-
    tiene_sintoma(U, fiebre, 2),
    tiene_sintoma(U, dolor_cabeza, 2),
    tiene_sintoma(U, rigidez_cuello, 1).

posible_enfermedad(U, bronquitis) :-
    fiebre_prolongada(U),
    tiene_sintoma(U, tos, 5),
    tiene_sintoma(U, dificultad_respiratoria, 3),
    tiene_sintoma(U, dolor_pecho, 1).

posible_enfermedad(U, gastroenteritis) :-
    tiene_sintoma(U, vomito, 1),
    tiene_sintoma(U, diarrea, 1),
    tiene_sintoma(U, dolor_abdominal, 1).

posible_enfermedad(U, dengue) :-
    fiebre_prolongada(U),
    tiene_sintoma(U, dolor_muscular, 3),
    tiene_sintoma(U, dolor_articulaciones, 3),
    tiene_sintoma(U, erupcion_cutanea, 1).

posible_enfermedad(U, rinitis_alergica) :-
    tiene_sintoma(U, estornudos, 1),
    tiene_sintoma(U, picazon_nasal, 1),
    tiene_sintoma(U, congestion, 1).

posible_enfermedad(U, amigdalitis) :-
    tiene_sintoma(U, fiebre, 2),
    tiene_sintoma(U, dolor_garganta, 2),
    tiene_sintoma(U, inflamacion_amigdalas, 1).

posible_enfermedad(U, sinusitis) :-
    tiene_sintoma(U, dolor_cabeza, 3),
    tiene_sintoma(U, congestion, 3),
    tiene_sintoma(U, dolor_facial, 3).

posible_enfermedad(U, infeccion_urinaria) :-
    tiene_sintoma(U, ardor_orinar, 2),
    tiene_sintoma(U, fiebre, 2),
    tiene_sintoma(U, dolor_lumbar, 2).

posible_enfermedad(U, hepatitis) :-
    tiene_sintoma(U, ictericia, 1),
    tiene_sintoma(U, fatiga, 2),
    tiene_sintoma(U, dolor_abdominal, 1).

posible_enfermedad(U, migrana) :-
    tiene_sintoma(U, dolor_cabeza, 1),
    tiene_sintoma(U, sensibilidad_luz, 1),
    tiene_sintoma(U, nausea, 1).

% ------------------------------------
% Reglas auxiliares basadas en duración
% ------------------------------------

% Verifica si un usuario tiene un síntoma con duración mínima 
tiene_sintoma(U, Sintoma, MinDias) :-
    registro_sintoma(U, Sintoma, Dias),
    Dias >= MinDias.

% Determina si el usuario tiene fiebre por más de 5 días
fiebre_prolongada(U) :-
    registro_sintoma(U, fiebre, Dias),
    Dias > 5.
