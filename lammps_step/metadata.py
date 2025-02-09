"""This file contains metadata to help describe the results of LAMMPS
calculations, etc.
"""

metadata = {}

"""Properties that LAMMPS produces, depending on the type of calculation.
"""

metadata["results"] = {
    "T": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "temperature",
        "dimensionality": "scalar",
        "property": "temperature#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "T,stderr": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "stderr of temperature",
        "dimensionality": "scalar",
        "property": "temperature, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "T,tau": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "autocorrelation time of temperature",
        "dimensionality": "scalar",
        "property": "temperature, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "T,inefficiency": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "statistical inefficiency of temperature sampling",
        "dimensionality": "scalar",
        "property": "temperature, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "P": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "pressure",
        "dimensionality": "scalar",
        "property": "pressure#LAMMPS#{model}",
        "type": "float",
        "units": "atm",
    },
    "P,stderr": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "stderr of pressure",
        "dimensionality": "scalar",
        "property": "pressure, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "atm",
    },
    "P,tau": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "autocorrelation time of pressure",
        "dimensionality": "scalar",
        "property": "pressure, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "P,inefficiency": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "statistical inefficiency of pressure sampling",
        "dimensionality": "scalar",
        "property": "pressure, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "density": {
        "calculation": ["npt"],
        "description": "pressure",
        "dimensionality": "scalar",
        "property": "density#LAMMPS#{model}",
        "type": "float",
        "units": "g/ml",
    },
    "density,stderr": {
        "calculation": ["npt"],
        "description": "stderr of density",
        "dimensionality": "scalar",
        "property": "density, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "density,tau": {
        "calculation": ["npt"],
        "description": "autocorrelation time of density",
        "dimensionality": "scalar",
        "property": "density, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "density,inefficiency": {
        "calculation": ["npt"],
        "description": "statistical inefficiency of density sampling",
        "dimensionality": "scalar",
        "property": "density, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "a": {
        "calculation": ["npt"],
        "description": "cell parameter 'a'",
        "dimensionality": "scalar",
        "property": "cell_a#LAMMPS#{model}",
        "type": "float",
        "units": "Å",
    },
    "a,stderr": {
        "calculation": ["npt"],
        "description": "stderr of cell 'a'",
        "dimensionality": "scalar",
        "property": "cell_a, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "a,tau": {
        "calculation": ["npt"],
        "description": "autocorrelation time of cell 'a'",
        "dimensionality": "scalar",
        "property": "cell_a, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "a,inefficiency": {
        "calculation": ["npt"],
        "description": "statistical inefficiency of cell 'a' sampling",
        "dimensionality": "scalar",
        "property": "cell_a, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "b": {
        "calculation": ["npt"],
        "description": "cell parameter 'b'",
        "dimensionality": "scalar",
        "property": "cell_b#LAMMPS#{model}",
        "type": "float",
        "units": "Å",
    },
    "b,stderr": {
        "calculation": ["npt"],
        "description": "stderr of cell 'b'",
        "dimensionality": "scalar",
        "property": "cell_b, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "b,tau": {
        "calculation": ["npt"],
        "description": "autocorrelation time of cell 'b'",
        "dimensionality": "scalar",
        "property": "cell_b, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "b,inefficiency": {
        "calculation": ["npt"],
        "description": "statistical inefficiency of cell 'b' sampling",
        "dimensionality": "scalar",
        "property": "cell_b, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "c": {
        "calculation": ["npt"],
        "description": "cell parameter 'c'",
        "dimensionality": "scalar",
        "property": "cell_c#LAMMPS#{model}",
        "type": "float",
        "units": "Å",
    },
    "c,stderr": {
        "calculation": ["npt"],
        "description": "stderr of cell 'c'",
        "dimensionality": "scalar",
        "property": "cell_c, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "c,tau": {
        "calculation": ["npt"],
        "description": "autocorrelation time of cell 'c'",
        "dimensionality": "scalar",
        "property": "cell_c, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "c,inefficiency": {
        "calculation": ["npt"],
        "description": "statistical inefficiency of cell 'c' sampling",
        "dimensionality": "scalar",
        "property": "cell_c, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "Etot": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "total energy",
        "dimensionality": "scalar",
        "property": "total energy#LAMMPS#{model}",
        "type": "float",
        "units": "kcal/mol",
    },
    "Etot,stderr": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "stderr of total energy",
        "dimensionality": "scalar",
        "property": "total energy, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "Etot,tau": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "autocorrelation time of total energy",
        "dimensionality": "scalar",
        "property": "total energy, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "Etot,inefficiency": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "statistical inefficiency of total energy sampling",
        "dimensionality": "scalar",
        "property": "total energy, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "Eke": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "kinetic energy",
        "dimensionality": "scalar",
        "property": "kinetic energy#LAMMPS#{model}",
        "type": "float",
        "units": "kcal/mol",
    },
    "Eke,stderr": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "stderr of kinetic energy",
        "dimensionality": "scalar",
        "property": "kinetic energy, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "Eke,tau": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "autocorrelation time of kinetic energy",
        "dimensionality": "scalar",
        "property": "kinetic energy, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "Eke,inefficiency": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "statistical inefficiency of kinetic energy sampling",
        "dimensionality": "scalar",
        "property": "kinetic energy, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "Epe": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "potential energy",
        "dimensionality": "scalar",
        "property": "potential energy#LAMMPS#{model}",
        "type": "float",
        "units": "kcal/mol",
    },
    "Epe,stderr": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "stderr of potential energy",
        "dimensionality": "scalar",
        "property": "potential energy, stderr#LAMMPS#{model}",
        "type": "float",
        "units": "K",
    },
    "Epe,tau": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "autocorrelation time of potential energy",
        "dimensionality": "scalar",
        "property": "potential energy, tau#LAMMPS#{model}",
        "type": "float",
        "units": "fs",
    },
    "Epe,inefficiency": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "statistical inefficiency of potential energy sampling",
        "dimensionality": "scalar",
        "property": "potential energy, inefficiency#LAMMPS#{model}",
        "type": "float",
        "units": "",
    },
    "Epair": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "nonbonded (vdW & electrostatic) energy",
        "dimensionality": "scalar",
        "type": "float",
        "units": "kcal/mol",
    },
    "Epair,stderr": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "stderr of nonbond energy",
        "dimensionality": "scalar",
        "type": "float",
        "units": "K",
    },
    "Epair,tau": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "autocorrelation time of nonbond energy",
        "dimensionality": "scalar",
        "type": "float",
        "units": "fs",
    },
    "Epair,inefficiency": {
        "calculation": [
            "nve",
            "nvt",
            "npt",
        ],
        "description": "statistical inefficiency of nonbond energy sampling",
        "dimensionality": "scalar",
        "type": "float",
        "units": "",
    },
}
