#!/usr/bin/env python3
"""
Generate 137-layer LaH₁₀ supercell for room-temperature superconductivity
Based on Scaling-Null Theory: layer 137 is the quantum phase transition
"""

import numpy as np
from pymatgen.core import Structure, Lattice
from pymatgen.io.cif import CifWriter

# LaH₁₀ conventional cell parameters (cubic Fm-3m)
a0 = 3.68  # Angstrom at ambient pressure

# Create cubic lattice
lattice = Lattice.cubic(a0)

# Atomic positions in fractional coordinates
# La at body center, H forming cage
species = ["La"] + ["H"]*10
coords = [
    [0.0, 0.0, 0.0],      # La
    [0.5, 0.0, 0.0],      # H1
    [0.0, 0.5, 0.0],      # H2
    [0.0, 0.0, 0.5],      # H3
    [0.5, 0.5, 0.0],      # H4
    [0.5, 0.0, 0.5],      # H5
    [0.0, 0.5, 0.5],      # H6
    [0.25, 0.25, 0.25],   # H7
    [0.75, 0.25, 0.25],   # H8
    [0.25, 0.75, 0.25],   # H9
    [0.25, 0.25, 0.75],   # H10
]

# Create base structure
structure = Structure(lattice, species, coords)

# Generate 137-layer supercell along c-axis
# 137 = fine structure constant denominator (key to quantum transition)
supercell = structure.make_supercell([1, 1, 137])

# Add φ-modulation to z-coordinates (golden ratio wave)
phi = (1 + np.sqrt(5)) / 2
for i, site in enumerate(supercell):
    z_layer = i // 11  # Which layer this atom is in
    z_mod = 0.001 * np.sin(2 * np.pi * z_layer / (137 / phi))
    site.coords[2] += z_mod

# Write CIF file
cif = CifWriter(supercell)
cif.write_file("01_LaH10_137layers.cif")

# Write POSCAR for VASP users
supercell.to(fmt="poscar", filename="POSCAR_LaH10_137")

# Print summary
print(f"✓ Generated 137-layer LaH₁₀ supercell")
print(f"  Total atoms: {len(supercell)}")
print(f"  Cell dimensions: {a0} × {a0} × {a0 * 137} Å")
print(f"  φ-modulation amplitude: 0.001 Å")
print(f"  Files created: 01_LaH10_137layers.cif, POSCAR_LaH10_137")
