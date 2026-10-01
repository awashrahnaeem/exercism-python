"""RNA transcription helpers.

This module converts a DNA strand into its RNA complement using a
lookup dictionary for each nucleotide pair.
"""


def method_2(dna_strand):
    """Return the RNA complement of the supplied DNA strand.

    Each DNA nucleotide is translated through a dictionary mapping:
    G -> C, C -> G, T -> A, and A -> U. The function turns the input
    into a single RNA string by joining the translated nucleotides in
    order.
    """
    nucleotide_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join(nucleotide_map[nucleotide] for nucleotide in dna_strand)


def to_rna(dna_strand):
    """Backward-compatible wrapper for the dictionary-based transcription method."""
    return method_2(dna_strand)

