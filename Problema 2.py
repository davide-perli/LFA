def positiv_vid(stare_initiala, stari_finale):
    if stare_initiala in stari_finale:
        return False  # Starea inițială este și stare finală, deci limbajul nu este vid

    visited = set()  # Stări vizitate
    stack = [stare_initiala]  # Stivele de explorare

    while stack:
        current_state = stack.pop()  # Extragem o stare din stivă
        if current_state in stari_finale:
            return False  # Am găsit o stare finală, deci limbajul nu este vid

        visited.add(current_state)  # Adăugăm starea curentă în setul de stări vizitate
        # Verificăm toate tranzacțiile din starea curentă și adăugăm stările accesibile în stivă
        for next_state in transitions.get(current_state, {}):
            if next_state not in visited:
                stack.append(next_state)

    # Dacă nu am găsit nicio stare finală accesibilă, limbajul este vid
    return True


# Incarcare date DFA
tranzitii = {}
with open("problema2_date.txt") as f:
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
            if start not in transitions:
                transitions[start] = {}
            transitions[start][letter] = end
            numar_tranzitii += 1  # Incrementare numar tranzitii

# Verificare dacă limbajul este vid
limbaj_vid = is_language_empty(initial_state, final_states)
print("Limbajul este vid." if limbaj_vid else "Limbajul nu este vid.")
