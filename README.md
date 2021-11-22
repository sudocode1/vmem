# vmem
VMem - Virtual Memory with a custom language inspired by Assembly.

## Example
This is an example program. With more developments to the language, this will be simplified. 
```vmem
CREATE BIT
CREATE BIT
CREATE BIT
INIT 0
SELECT 0
SET 2
INIT 1

SELECT 1
CALCULATION MULTIPLY 0 0
READ BIT
COPY 2
RELEASE

INIT 1
SELECT 1
CALCULATION MULTIPLY 0 2
READ BIT
SELECT 2
RELEASE
SELECT 1
COPY 2
RELEASE

INIT 1
SELECT 1
CALCULATION MULTIPLY 0 2
READ BIT
SELECT 2
RELEASE
SELECT 1
COPY 2
RELEASE
```

## Language
### Directly with MEMORY
These commands will let you work with the MEMORY, rather than with specific bits. 
#### `CREATE BIT`
CREATE BIT will create a bit within MEMORY, creating a singular `None` bit, which you will then need to initialise to use.
#### `CREATE BYTE`
CREATE BYTE will run CREATE BIT eight times, bringing you to the maximum amount of possible bits in MEMORY.
#### `INIT <BIT>`
INIT <BIT> will intiailise the bit entered, setting it to 0, so you can then select & utilise it.
#### `SELECT <BIT>`
SELECT <BIT> will allow you to select an initialized bit, allowing you to utilise it.
#### `READ BYTE`
READ BYTE will output the MEMORY in the state it is in.
#### `DESTROY MEMORY`
DESTROY MEMORY will reset the MEMORY back to 0 bits.

### Bit utilisation
These commands can be used once a bit is selected.
#### `SET <number>`
SET <number> will allow you to set the bit selected as the number specific.
#### `RELEASE`
RELEASE will set the bit back to an uninitialized state. You will have to select a new bit after this.
#### `CALCULATION <CALC> <BIT> <BIT>`
CALCULATION <CALC> <BIT> <BIT> will allow you to do <CALC> (e.g. ADDITION) to the two bits specific and set the result as the bit selected.
#### `READ BIT`
READ BIT will output the value of the selected bit.
#### `INCREMENT`
INCREMENT will add 1 to the selected bit.
#### `DECREMENT`
DECREMENT will take 1 from the selected bit.
#### `COPY <BIT>`
COPY <BIT> will copy the value of the selected bit into the specified bit.

### Other
These are misc commands that can be used for convinience.
#### `DEBUG`
DEBUG will toggle debug mode.
