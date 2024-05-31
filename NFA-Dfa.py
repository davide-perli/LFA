def nfa_to_dfa(nfa_transitions, nfa_initial_state, nfa_final_states, nfa_states, nfa_letters):
    # Inițializează tranzițiile DFA ca un dicționar gol
    dfa_transitions = {}

    # Starea inițială a DFA-ului este un set care conține starea inițială a NFA-ului
    dfa_initial_state = frozenset([nfa_initial_state])

    # Inițializează setul de stări finale ale DFA-ului
    dfa_final_states = set()

    # Listă cu stările DFA neprocesate, începe cu starea inițială a DFA-ului
    unprocessed_states = [dfa_initial_state]

    # Set de stări DFA, începe cu starea inițială
    dfa_states = set()
    dfa_states.add(dfa_initial_state)

    # Procesarea fiecărei stări DFA
    while unprocessed_states:
        # Scoate o stare DFA neprocesată din listă
        current_dfa_state = unprocessed_states.pop()

        # Dacă starea curentă nu are tranziții definite, inițializează-le ca un dicționar gol
        if current_dfa_state not in dfa_transitions:
            dfa_transitions[current_dfa_state] = {}

        # Pentru fiecare literă din alfabetul NFA
        for letter in nfa_letters:
            next_state = set()

            # Pentru fiecare stare NFA din starea curentă DFA
            for nfa_state in current_dfa_state:
                # Verifică toate tranzițiile din starea NFA curentă
                for transition in nfa_transitions.get(nfa_state, []):
                    if transition[0] == letter:
                        # Adaugă starea de destinație la următoarea stare DFA
                        next_state.add(transition[1])

            # Convertește next_state în frozenset pentru a fi utilizat ca cheie în dicționare
            next_state = frozenset(next_state)

            if next_state:
                # Adaugă tranziția la dfa_transitions
                dfa_transitions[current_dfa_state][letter] = next_state

                # Dacă next_state nu a fost deja adăugată la dfa_states
                if next_state not in dfa_states:
                    dfa_states.add(next_state)
                    unprocessed_states.append(next_state)

                # Dacă next_state conține oricare dintre stările finale ale NFA, adaugă next_state la dfa_final_states
                if next_state & nfa_final_states:
                    dfa_final_states.add(next_state)

    # Returnează tranzițiile DFA, starea inițială DFA, stările finale DFA și toate stările DFA
    return dfa_transitions, dfa_initial_state, dfa_final_states, dfa_states


# Citirea NFA-ului din fișier
nfa_transitions = {}
words = []
with open("data.in") as f:
    # Citirea numărului de stări și stările
    number_of_states = int(f.readline())
    states = [int(state) for state in f.readline().split()]

    # Citirea numărului de litere și literele
    number_of_letters = int(f.readline())
    letters = [letter for letter in f.readline().split()]

    # Citirea stării inițiale
    initial_state = int(f.readline())

    # Citirea numărului de stări finale și stările finale
    number_of_final_states = int(f.readline())
    final_states = {int(final_state) for final_state in f.readline().split()}

    # Citirea tranzițiilor
    number_of_transitions = int(f.readline())
    for i in range(number_of_transitions):
        start, letter, finish = f.readline().split()
        start, finish = int(start), int(finish)
        if start not in nfa_transitions:
            nfa_transitions[start] = []
        nfa_transitions[start].append((letter, finish))

    # Citirea cuvintelor de testat
    number_of_tests = int(f.readline())
    for i in range(number_of_tests):
        words.append(f.readline().strip())

# Conversia NFA-ului în DFA
dfa_transitions, dfa_initial_state, dfa_final_states, dfa_states = nfa_to_dfa(
    nfa_transitions, initial_state, final_states, states, letters
)

# Output DFA details
with open("data.out", "w") as g:
    g.write(f"Initial State: {dfa_initial_state}\n")
    g.write(f"States: {sorted(map(str, dfa_states))}\n")
    g.write("Transitions:\n")
    for state, transitions in dfa_transitions.items():
        for letter, next_state in transitions.items():
            g.write(f"  {state} --{letter}--> {next_state}\n")
    g.write(f"Final States: {sorted(map(str, dfa_final_states))}\n")

# # Testarea cuvintelor pe DFA
# with open("data.out", "w") as g:
#     for word in words:
#         current_state = dfa_initial_state
#
#         # Procesarea fiecărei litere din cuvânt
#         for letter in word:
#             if letter in dfa_transitions[current_state]:
#                 # Actualizează starea curentă
#                 current_state = dfa_transitions[current_state][letter]
#             else:
#                 # Dacă nu există tranziție pentru litera curentă, cuvântul nu este acceptat
#                 g.write("NU\n")
#                 break
#         else:
#             # Dacă bucla nu s-a întrerupt, verifică dacă starea curentă este finală
#             if any(state in dfa_final_states for state in current_state):
#                 g.write("DA\n")
#             else:
#                 g.write("NU\n")
