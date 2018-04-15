# tom
Implementation of Tomasulo's Algorithm in Python - 3


Uses the following values...

|                                                             |       |                |                 |           |                 |                  |
|-------------------------------------------------------------|-------|----------------|-----------------|-----------|-----------------|------------------|
| Component Name                                              | Area  | Internal Power | Switching Power | Max Delay | PDP E-21 Joules | ADP E-24 m^2 s^2 |
|                                                             | E-18  | E-9 W          | E-9 W           | ps        |                 |                  |
| Prefix adder                                                | 1827  | 30886          | 35495           | 143       | 64849365        | 261261           |
| Wallace Tree Multiplier                                     | 25943 | 507545         | 73117           | 168       | 1896874331      | 4358424          |
| FP Multiplier                                               | 18024 | 379432         | 459556          | 4209      | 8283037344      | 75863016         |
| FP Adder                                                    | 3943  | 51955          | 65801           | 1298      | 259453343       | 5118014          |
| Shifter                                                     | 1727  | 37588          | 41927           | 103       | 72407929        | 177881           |
|                                                             |       |                |                 |           |                 |                  |
| ALU (With Tristate gates instead of a mux to choose module) | 4652  | 394516         | 544262          | 671       | 2531906824      | 3121492          |
| Processor Unsynthesizable (Undriven Bits)                   | -     | -              | -               | -         |                 |                  |
| Done by CED15I007 & 29                                      |       |                |                 |           |                 |                  |
