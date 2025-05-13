# 4-mer-String-Reconstruction-from-de-Bruijn-Graph

# Description

This Python script reconstructs a linear string from a given set of 4-mers (substrings of length 4) by creating a de Bruijn graph and finding an Eulerian path through it. The script uses Hierholzer's algorithm to find the Eulerian path, which is then used to reconstruct the original sequence. This method is typically used in bioinformatics for genome assembly.

Usage

Example:

```

kmers = [
    "AAAT", "AATG", "ACCC", "ACGC", "ATAC",
    "ATCA", "ATGC", "CAAA", "CACC", "CATA",
    "CATC", "CCAG", "CCCA", "CGCT", "CTCA",
    "GCAT", "GCTC", "TACG", "TCAC", "TCAT", "TGCA"
]

linear_string = construct_linear_string(kmers)
print(linear_string)
```

# Output:
AAATGCATCATACGCTCACCCAG


# Function: 
```

def construct_linear_string(kmers):
    # Create a de Bruijn graph
    graph = create_de_bruijn_graph(kmers)

    # Find an Eulerian path in the graph
    path = find_eulerian_path(graph)

    # Reconstruct the linear string from the Eulerian path
    linear_string = reconstruct_from_path(path)

    return linear_string


```

    
# Applications


* Genome assembly and sequence reconstruction.
* Bioinformatics pipelines for short-read sequencing.
* Data analysis for overlapping k-mer problems.

# License

* This project is licensed under the MIT License.
