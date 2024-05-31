def complement_dfa(stari_finale, stari_totale):
    complement_stari_finale = []
    for state in stari_totale:
        if state not in stari_finale:
            complement_stari_finale.append(state)
    return complement_stari_finale


def write_complement_dfa_to_file(stari, alfabet, stare_initiala, stari_finale, file_path):
    with open(file_path, "w") as r:
        r.write(f"{len(stari)}\n")
        r.write(" ".join(str(state) for state in sorted(stari)) + "\n")
        r.write(f"{len(alfabet)}\n")
        r.write(" ".join(alfabet) + "\n")
        r.write(f"{stare_initiala}\n")
        r.write(f"{len(stari_finale)}\n")
        r.write(" ".join(str(state) for state in sorted(stari_finale)) + "\n")
        r.write(f"{sum(len(tranzitii[state]) for state in tranzitii)}\n")
        for start_state, state_transitions in tranzitii.items():
            for letter, end_state in state_transitions.items():
                r.write(f"{start_state} {letter} {end_state}\n")


# Incarcare date DFA
tranzitii = {}
with open("problema1_date.txt") as f:
    numar_stari = int(f.readline())
    states = [int(state) for state in f.readline().split()]

    numar_litere = int(f.readline())
    letters = [letter for letter in f.readline().split()]

    initial_state = int(f.readline())

    numar_stari_finale = int(f.readline())
    final_states = [int(final_state) for final_state in f.readline().split()]

    numar_tranzitii = 0  # Schimbare pentru a număra tranzacțiile corect
    for line in f:  # Citeste fiecare linie din fisier
        parts = line.split()  # Imparte linia in parti
        if len(parts) == 3:  # Verifica daca linia contine o tranzitie valida
            start, letter, end = parts  # Extrage starea de start, litera si starea finala
            start, end = int(start), int(end)
            if start not in tranzitii:
                tranzitii[start] = {}
            tranzitii[start][letter] = end
            numar_tranzitii += 1  # Incrementare numar tranzitii

# Creare complement DFA
complement_final_states = complement_dfa(final_states, states)

# Scriere DFA in fisier
write_complement_dfa_to_file(states, letters, initial_state, complement_final_states, "complement_dfa_data.out")
