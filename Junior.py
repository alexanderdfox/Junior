from Bio.Seq import Seq
import random
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
pairing = "male_female"  # Options: "male_female", "two_males", "two_females"
sequence_length = 100
mutation_rate = 0.01

# Generate a DNA sequence of given length
def generate_dna_seq(length=100):
	return Seq(''.join(random.choice("ATCG") for _ in range(length)))

# Recombine two sequences with crossover
def recombine(seq1, seq2):
	point = random.randint(1, len(seq1) - 1)
	return seq1[:point] + seq2[point:], point

# Apply mutations
def mutate(sequence, mutation_rate=0.01):
	mutated = []
	for base in sequence:
		if random.random() < mutation_rate:
			mutated.append(random.choice("ATCG".replace(base, "")))
		else:
			mutated.append(base)
	return Seq(''.join(mutated))

# Plot crossover
def plot_recombination(original1, original2, result, point, label):
	plt.figure(figsize=(10, 1.5))
	plt.title(f"{label} Recombination at index {point}")
	plt.axvline(x=point, color='red', linestyle='--', label='Crossover')
	plt.text(point + 1, 0.2, '⟵ from parent 1\n⟶ from parent 2', color='red')
	plt.plot([0, len(original1)], [0, 0], color='green', linewidth=3)
	plt.xlim(0, len(original1))
	plt.yticks([])
	plt.xlabel('Nucleotide Index')
	plt.legend()
	plt.show()

# --- Generate Sequences Based on Pairing ---
if pairing == "male_female":
	print("🧬 Simulating Male + Female")
	mom1, mom2 = generate_dna_seq(sequence_length), generate_dna_seq(sequence_length)
	dad1, dad2 = generate_dna_seq(sequence_length), generate_dna_seq(sequence_length)
	
	gamete1, point1 = recombine(mom1, mom2)  # Egg
	gamete2, point2 = recombine(dad1, dad2)  # Sperm

elif pairing == "two_males":
	print("🧬 Simulating Two Males (Sperm + Sperm)")
	male1a, male1b = generate_dna_seq(sequence_length), generate_dna_seq(sequence_length)
	male2a, male2b = generate_dna_seq(sequence_length), generate_dna_seq(sequence_length)
	
	gamete1, point1 = recombine(male1a, male1b)
	gamete2, point2 = recombine(male2a, male2b)

elif pairing == "two_females":
	print("🧬 Simulating Two Females (Egg + Egg)")
	female1a, female1b = generate_dna_seq(sequence_length), generate_dna_seq(sequence_length)
	female2a, female2b = generate_dna_seq(sequence_length), generate_dna_seq(sequence_length)
	
	gamete1, point1 = recombine(female1a, female1b)
	gamete2, point2 = recombine(female2a, female2b)

else:
	raise ValueError("Invalid pairing type. Choose: 'male_female', 'two_males', or 'two_females'.")

# Combine gametes and mutate
child_dna = mutate(gamete1 + gamete2, mutation_rate)

# --- Output ---
print("\nGamete 1:", gamete1)
print("Gamete 2:", gamete2)
print("\n👶 Child DNA:", child_dna)

# --- Visualize ---
plot_recombination(gamete1[:sequence_length], gamete1[sequence_length:], gamete1, point1, "Gamete 1")
plot_recombination(gamete2[:sequence_length], gamete2[sequence_length:], gamete2, point2, "Gamete 2")
