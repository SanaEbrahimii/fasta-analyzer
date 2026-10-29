import csv


def read_fasta(path):
    records = []
    name = None
    parts = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    records.append((name, "".join(parts).upper()))
                name = line[1:]
                parts = []
            else:
                parts.append(line)
    if name is not None:
        records.append((name, "".join(parts).upper()))
    return records


def gc_percent(seq):
    if not seq:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return 100 * gc / len(seq)


BASES = "TCAG"
AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

CODON_TABLE = {}
i = 0
for a in BASES:
    for b in BASES:
        for c in BASES:
            CODON_TABLE[a + b + c] = AMINO[i]
            i += 1


def translate(seq):
    protein = ""
    for i in range(0, len(seq) - len(seq) % 3, 3):
        codon = seq[i:i + 3]
        protein += CODON_TABLE.get(codon, "X")
    return protein


def main():
    records = read_fasta("sequences.fasta")

    print(f"{'id':<8}{'length':>7}{'GC%':>8}  AA sequence")
    for name, seq in records:
        print(f"{name:<8}{len(seq):>7}{gc_percent(seq):>8.2f}  {translate(seq)}")

    with open("results.csv", "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["id", "length", "gc_percent", "aa_sequence"])
        for name, seq in records:
            writer.writerow([name, len(seq), round(gc_percent(seq), 2), translate(seq)])


if __name__ == "__main__":
    main()

