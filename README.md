# CallGraphGenerator

This small utility emits a call graph in JSON

Basic usage:

    ./generate_call_graph.sh <binaryName> [rootFunction=main]

JSON is written to stdout

By default, the root function will be `main` but many executables don't use `main`. You can specify the root function to construct the call graph from as the *second* argument.

Recursion is handled by not expanding on functions already emitted in the DFS hierarchy of the graph.
