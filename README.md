## <ins>Compiler Visualizer</ins>

### Getting Started
```
    open python interpreter in the root folder and run shell.py
```
#### Example input & Output :
```buildoutcfg
comviz >VAR age = 20
[(KEYWORD: VAR), (ID: age), (EQ: =), (int: 20), (EOF)]

E
├── (KEYWORD: VAR)
├── (ID: age)
├── (EQ: =)
└── ArE
    └── T
        └── F
            └── P
                └── A
                    └── (int: 20)
20
comviz >age + 30 - 10
E
└── C
    └── ArE
        ├── T
        │   └── F
        │       └── P
        │           └── A
        │               └── (ID: age)
        ├── (PLUS: +)
        ├── T
        │   └── F
        │       └── P
        │           └── A
        │               └── (int: 30)
        ├── (MINUS: -)
        └── T
            └── F
                └── P
                    └── A
                        └── (int: 10)
40                    
```

[comment]: <> (## Demo v1.0)

[comment]: <> ([![Demo Video]&#40;https://j.gifs.com/JymVGy.gif&#41;]&#40;https://www.youtube.com/watch?v=E4tB00eulAE&#41;)

[comment]: <> (=======)

