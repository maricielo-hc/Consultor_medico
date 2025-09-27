% ============================
% Base de conocimiento
% Sistema Experto de Síntomas
% ============================

% Reglas de diagnóstico
enfermedad(neumonia) :- fiebre, tos, dificultad_respiratoria.
enfermedad(covid) :- fiebre, dolor_muscular, anosmia.
enfermedad(apendicitis) :- dolor_abdominal, vomito, dolor_hipocondrio_derecho.
enfermedad(meningitis) :- dolor_cabeza, rigidez_cuello, fiebre.

% Síntomas como predicados dinámicos
:- dynamic fiebre/0.
:- dynamic tos/0.
:- dynamic dificultad_respiratoria/0.
:- dynamic dolor_muscular/0.
:- dynamic anosmia/0.
:- dynamic dolor_abdominal/0.
:- dynamic vomito/0.
:- dynamic dolor_hipocondrio_derecho/0.
:- dynamic dolor_cabeza/0.
:- dynamic rigidez_cuello/0.

