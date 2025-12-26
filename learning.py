# AI introducing himself:
Name = "Python AI"
Version = "1.0"
Description = "An AI developed to assist with Python programming and learning."

def introduce():
    return f"Hello! I am {Name}, version {Version}. {Description}"

print(introduce())

# Pause and ask for user input:
input("\nHow can I assist you with Python programming today? Press Enter to continue...")

# Main conversation
user_question = input("Type your question: ")

AI_led_response = "I can teach you Python basics!"
print(AI_led_response)
print("\n" + "="*50)

# ========== TOPIC 1: HELLO WORLD ==========
learn_hello = input("\n🔹 Want to learn about Hello World? (yes/no/exit): ")

if learn_hello.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_hello.lower() == 'yes':
    print("\n" + "="*50)
    print("1. Hello World Example:")
    print('   print("Hello, World!")')
    
    print("\n   💡 Explanation:")
    
    def explain_hello_world():
        print("\n" + "=" * 50)
        print("🖨️ THE 'HELLO WORLD' PROGRAM")
        
        print("""
        🌍 WHAT IS HELLO WORLD?
        This is the TRADITIONAL first program everyone writes 
        when learning a new programming language.
        
        ✨ WHY DO WE START WITH IT?
        • It's SIMPLE: Just one line of code
        • It's EXCITING: You see immediate results
        • It's FOUNDATIONAL: Teaches the most basic command
        
        🔧 BREAKDOWN:
        print() = Your CODE'S MOUTH that speaks to the screen
        "Hello, World!" = The WORDS you want to say
        Parentheses () = Holds what you want to print
        
        💡 THINK OF IT AS:
        Your computer is a QUIET ROBOT 🤖
        print() is the SPEAKER 🔊 you install
        "Hello, World!" is its FIRST WORDS 👶
        
        🎬 THE MAGIC MOMENT:
        When you run this, your silent computer 
        suddenly SPEAKS to you for the first time!
        """)
        
        see_example = input("\nWant to see the code breakdown? (yes/no): ")
        if see_example.lower() == 'yes':
            print("\n📝 CODE EXAMPLE:")
            print('   print("Hello, World!")')
            print("   ↑         ↑")
            print("   Command   Message")
        else:
            print("Skipping code breakdown...")
        
        print("\n" + "=" * 50)
        print("TRY IT! Type: print('Your Name Here')")
        print("=" * 50)
    
    explain_hello_world()
    
    AI_response = "Awesome! You've learned how to print text in Python."
    print(AI_response)
else:
    print("Skipping Hello World...")

# ========== TOPIC 2: FUNCTIONS ==========
learn_functions = input("\n🔹 Want to learn about Functions? (yes/no/exit): ")

if learn_functions.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_functions.lower() == 'yes':
    print("\n" + "="*50)
    print("2. Functions in Python:")
    
    def explain_functions():
        print("\n   📦 What are functions?")
        print("\n🤖 FUNCTIONS = YOUR CODING ASSISTANTS")
        print("=" * 50)
        
        print("""
        🎯 WHAT ARE FUNCTIONS?
        Functions are like TRAINED ASSISTANTS in your code. They are:
        - BLOCKS OF CODE that do a SPECIFIC JOB
        - REUSABLE: Call them anytime you need to do a specific task
        - PARAMETERIZED: They can take INPUTS to work with
        - RETURN VALUES: They can GIVE BACK OUTPUTS after processing
        
        • ONE-TIME TRAINING: Teach them a skill once
        • LIFETIME SERVICE: Use that skill forever
        • TIME TRAVEL: Save hours of repeating work
        
        🍞 REAL-LIFE EXAMPLE: TOASTER
        1. You BUY a toaster (create function)
        2. You PUT in bread (give input)
        3. Toaster DOES its magic (process inside)
        4. You GET toast (receive output)
        
        🔧 IN PROGRAMMING:
        - CREATE function once with 'def'
        - GIVE it data to work with (parameters)
        - GET back results (return value)
        - USE it anytime, anywhere!
        """)
        
        print("\n" + "💡 REMEMBER: If you do something MORE THAN ONCE,")
        print("             make it a FUNCTION!")
        
        see_example = input("\nWant to see a function example? (yes/no): ")
        if see_example.lower() == 'yes':
            print("\n   🔧 Function Example:")
            print("   def greet(name):")
            print("       return f'Hello, {name}!'")
            print("   ")
            print("   # Using the function:")
            print("   print(greet('Alice'))")
            print("   # Output: Hello, Alice!")
        else:
            print("Skipping example...")
    
    explain_functions()
    
    AI_response = "Awesome! You've learned about functions and how to create and use them."
    print(AI_response)
else:
    print("Skipping Functions...")

# ========== TOPIC 3: VARIABLES ==========
learn_variables = input("\n🔹 Want to learn about Variables? (yes/no/exit): ")

if learn_variables.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_variables.lower() == 'yes':
    print("\n" + "="*50)
    print("3. Variables in Python:")
    
    def explain_variables():
        print("\n   🏷️ What are variables?")
        print("\n📦 VARIABLES: YOUR CODE'S STORAGE BOXES")
        print("=" * 50)
        
        print("""
        🎯 WHAT ARE VARIABLES?
        Variables are like LABELED STORAGE BOXES 📦
        You put things in them, give them a NAME TAG,
        and find them later using the name!
        
        🏪 REAL-LIFE EXAMPLE: SUPERMARKET LOCKERS
        1. You put your bag in a locker (STORE value)
        2. You get a ticket with number 42 (VARIABLE name)
        3. Later, show ticket 42 (USE variable)
        4. Get your bag back (RETRIEVE value)
        
        🔑 KEY IDEA: 
        The LOCKER NUMBER is the VARIABLE NAME (age, name, score)
        The BAG INSIDE is the VARIABLE VALUE (18, "Ali", 95.5)
        
        📊 TYPES OF BOXES (DATA TYPES):
        • 📝 STRING BOX: For text → name = "Qasim"
        • 🔢 INTEGER BOX: For whole numbers → age = 18  
        • 📐 FLOAT BOX: For decimals → height = 5.9
        • ✅ BOOLEAN BOX: For True/False → is_student = True
        
        💡 WHY USE VARIABLES?
        1. REUSE DATA: Store once, use many times
        2. CLARITY: Descriptive names explain themselves
        3. FLEXIBILITY: Change value in one place
        4. ORGANIZATION: Keeps your code tidy
        """)
        
        see_examples = input("\nWant to see variable examples? (yes/no): ")
        if see_examples.lower() == 'yes':
            print("\n📝 REAL EXAMPLE:")
            print("   name = 'Muhammad Qasim'   ← STRING variable")
            print("   age = 18                   ← INTEGER variable")
            print("   score = 95.5               ← FLOAT variable")
            print("   passed = True              ← BOOLEAN variable")
        else:
            print("Skipping examples...")
        
        print("\n" + "=" * 50)
        print("VARIABLES REMEMBER SO YOU DON'T HAVE TO!")
        print("=" * 50)
    
    explain_variables()
    
    AI_response = "Great job! You've learned about variables and their types."
    print(AI_response)
else:
    print("Skipping Variables...")

# ========== TOPIC 4: RELATIONAL OPERATORS ==========
learn_operators = input("\n🔹 Want to learn about Relational Operators? (yes/no/exit): ")

if learn_operators.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_operators.lower() == 'yes':
    print("\n" + "="*50)
    print("4. Relational Operators in Python:")
    
    def explain_relational_operators():
        print("\n   🔍 What are relational operators?")
        print("\n🔍 RELATIONAL OPERATORS: CODE'S COMPARISON TOOLS")
        print("=" * 50)
        
        print("""
        🎯 WHAT ARE THEY?
        These are CODE'S QUESTION WORKS that compare values
        and answer with TRUE 👍 or FALSE 👎
        
        👨🏫 THINK LIKE A TEACHER GRADING PAPERS:
        • Is score1 EQUAL TO score2? (==)
        • Is Ali's height GREATER THAN Sara's? (>)
        • Is age1 LESS THAN age2? (<)
        
        🔧 THE COMPARISON TOOLKIT:
        ==  EQUAL TO           → "Are these TWINS?" 👯
        !=  NOT EQUAL TO       → "Are they DIFFERENT?" 🚫
        >   GREATER THAN       → "Who is TALLER?" 📏
        <   LESS THAN          → "Who is YOUNGER?" 👶
        >=  GREATER OR EQUAL   → "Passing grade OR higher?" 🎓
        <=  LESS OR EQUAL      → "Child ticket age limit?" 🎫
        
        🎮 REAL-LIFE DECISIONS:
        • CAN YOU VOTE? → age >= 18
        • IS THE DOOR LOCKED? → door_status == "locked"
        • IS THE CUP FULL? → water_level >= cup_capacity
        
        💡 SECRET: Computers are DUMB at thinking
        but SMART at COMPARING! These operators 
        give computers DECISION-MAKING POWER!
        """)
        
        see_examples = input("\nWant to see practical examples? (yes/no): ")
        if see_examples.lower() == 'yes':
            print("\n📝 PRACTICAL EXAMPLES:")
            print("   age = 18")
            print("   can_vote = age >= 18      # True ✓")
            print("   is_minor = age < 18       # False ✗")
            print("   is_teenager = age >= 13 and age <= 19  # True ✓")
        else:
            print("Skipping examples...")
        
        print("\n" + "=" * 50)
        print("EVERY 'IF' DECISION USES THESE OPERATORS!")
        print("=" * 50)
        
        # MOVED THIS INSIDE THE FUNCTION (FIX #2)
        print("\n" + "=" * 50)
        AI_response = "Of course! Relational operators compare two values and return True or False based on the comparison."
        print(AI_response)
        print("\n   💡 Explanation:")
        print("   - Relational operators compare two values")
        print("   - Useful in decision-making and control flow")
    
    explain_relational_operators()
else:
    print("Skipping Relational Operators...")

# ========= TOPIC 5: Assignment Operators ==========
learn_assignment = input("\n🔹 Want to learn about Assignment Operators? (yes/no/exit): ")
if learn_assignment.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_assignment.lower() == 'yes':
    print("\n" + "="*50)
    print("5. Assignment Operators in Python:")
    
    def explain_assignment_operators():
        print("\n   📝 What are assignment operators?")
        print("\n📝 ASSIGNMENT OPERATORS: CODE'S VALUE ASSIGNERS")
        print("=" * 50)
        
        print("""
        🎯 WHAT ARE THEY?
        Assignment operators are used to ASSIGN VALUES
        to VARIABLES in your code.
        
        🔧 THE ASSIGNMENT TOOLKIT:
        =    SIMPLE ASSIGNMENT       → x = 5          # Assigns 5 to x
        +=   ADD AND ASSIGN          → x += 3         # x = x + 3
        -=   SUBTRACT AND ASSIGN     → x -= 2         # x = x - 2
        *=   MULTIPLY AND ASSIGN     → x *= 4         # x = x * 4
        /=   DIVIDE AND ASSIGN       → x /= 2         # x = x / 2
        %=   MODULUS AND ASSIGN      → x %= 3         # x = x % 3
        //=  FLOOR DIVIDE AND ASSIGN → x //= 2        # x = x // 2
        **=  EXPONENTIATE AND ASSIGN → x **= 3        # x = x ** 3
        
        💡 EXAMPLE USAGE:
        x = 10
        x += 5    # Now x = 15
        x *= 2    # Now x = 30
        print(x)  # Output: 30
        
        🔑 SIMPLE RULE:
        These are SHORTCUTS for updating variables!
        """)
        
        print("\n" + "=" * 50)
        print("Assignment operators make your code SHORTER!")
        print("=" * 50)
    
    explain_assignment_operators()
    
    print("\nGreat! You learned about assignment operators!")
else:
    print("Skipping Assignment Operators...")

# ========= TOPIC 6: LOGICAL OPERATORS ==========
learn_logical = input("\n🔹 Want to learn about Logical Operators? (yes/no/exit): ")
if learn_logical.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_logical.lower() == 'yes':
    print("\n" + "="*50)
    print("6. Logical Operators in Python:")
    
    def explain_logical_operators():
        print("\n   🤔 What are logical operators?")
        print("\n🤔 LOGICAL OPERATORS: CODE'S THINKING TOOLS")
        print("=" * 50)
        
        print("""
        🎯 WHAT ARE THEY?
        Logical operators help your code MAKE DECISIONS
        by combining multiple conditions.
        
        🔧 THE LOGICAL TOOLKIT:
        and  LOGICAL AND       → True if BOTH conditions are True
        or   LOGICAL OR        → True if AT LEAST ONE condition is True
        not  LOGICAL NOT       → Inverts the truth value
        
        💡 EXAMPLE USAGE:
        age = 20
        has_id = True
        
        # Check if eligible to enter club
        can_enter = (age >= 18) and has_id   # True ✓
        
        # Check if eligible for discount
        is_student = False
        eligible_discount = (age < 18) or is_student  # False ✗
        
        # Invert a condition
        is_not_adult = not (age >= 18)  # False ✗
        
        🔑 SIMPLE RULE:
        Use logical operators to COMBINE CONDITIONS!
        """)
        
        print("\n" + "=" * 50)
        print("Logical operators help your code THINK SMARTER!")
        print("=" * 50)
    
    explain_logical_operators()  # FIX #1: ADDED THIS MISSING FUNCTION CALL
    
    print("\nGreat! You learned about logical operators!")
else:
    print("Skipping Logical Operators...")

# ==== TOPIC 7: TYPE CONVERSION ===========
learn_type_conversion = input("\n🔹 Want to learn about Type Conversion? (yes/no/exit): ")
if learn_type_conversion.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_type_conversion.lower() == 'yes':
    print("\n" + "="*50)
    print("7. Type Conversion in Python:")
    
    def explain_type_conversion():
        print("\n   🔄 What is type conversion?")
        print("\n🔄 TYPE CONVERSION: CHANGING DATA TYPES")
        print("=" * 50)
        
        print("""
        🎯 WHAT IS IT?
        Type conversion is changing a variable from 
        one DATA TYPE to another.
        
        📋 TWO TYPES OF CONVERSION:
        
        1️⃣ IMPLICIT CONVERSION (Automatic)
        Python does it automatically when needed.
        
        Example:
        num_int = 10      # Integer
        num_float = 5.5   # Float
        result = num_int + num_float  # Python converts 10 → 10.0
        print(result)     # Output: 15.5 (Float)
        
        2️⃣ EXPLICIT CONVERSION (Manual)
        YOU control it using functions.
        
        🔧 EXPLICIT CONVERSION FUNCTIONS:
        int()     → Converts to INTEGER
        float()   → Converts to FLOAT  
        str()     → Converts to STRING
        bool()    → Converts to BOOLEAN
        
        💻 EXAMPLES:
        # String to Integer
        age_str = "25"
        age_int = int(age_str)      # "25" → 25
        
        # Integer to String  
        score = 95
        score_str = str(score)      # 95 → "95"
        
        # Float to Integer (cuts decimal)
        price = 19.99
        price_int = int(price)      # 19.99 → 19
        
        💡 PRACTICAL USE:
        • User input is ALWAYS string → Convert to numbers
        • Calculations need numbers → Convert strings
        • Display numbers in text → Convert to strings
        
        ⚠️ COMMON ERRORS:
        int("hello")   # ❌ Error: Can't convert text to number!
        int("10.5")    # ❌ Error: Use float() first!
        """)
        
        print("\n" + "=" * 50)
        print("Implicit = Python decides, Explicit = YOU decide!")
        print("=" * 50)
    
    explain_type_conversion()
    
    print("\nGreat! You learned about type conversion!")
else:
    print("Skipping Type Conversion...")

# ========= TOPIC 8: INPUT FUNCTION ==========
learn_input_function = input("\n🔹 Want to learn about the Input Function? (yes/no/exit): ")
if learn_input_function.lower() == 'exit':
    print("\n👋 Session ended. Goodbye!")
    exit()
elif learn_input_function.lower() == 'yes':
    print("\n" + "="*50)
    print("8. Input Function in Python:")
    
    def explain_input_function():
        print("\n   🖊️ What is the input function?")
        print("\n🖊️ INPUT FUNCTION: GETTING USER DATA")
        print("=" * 50)
        
        print("""
        🎯 WHAT IS IT?
        The input() function allows your program to 
        TAKE INPUT from the user during execution.
        
        🔧 HOW TO USE IT:
        syntax: variable = input("Prompt message: ")
        
        💡 EXAMPLE USAGE:
        name = input("Enter your name: ")   # User types their name
        print("Hello, " + name + "!")        # Greets the user
        
        age = input("Enter your age: ")      # User types their age
        age_next_year = int(age) + 1         # Convert to int and add 1
        print("Next year, you will be " + str(age_next_year) + " years old.")
        
        🔑 IMPORTANT NOTE:
        The input() function ALWAYS returns a STRING.
        Convert to other types (int, float) as needed!
        
        ⚠️ COMMON MISTAKES:
        age = input("Enter your age: ")
        next_age = age + 1   # ❌ Error: Can't add int to str!
        
        Correct way:
        age = int(input("Enter your age: "))
        next_age = age + 1   # ✅ Works perfectly!
        """)
        
        print("\n" + "=" * 50)
        print("Input function makes your program INTERACTIVE!")
        print("=" * 50)
    
    explain_input_function()
    
    print("\nGreat! You learned about the input function!")
else:
    print("Skipping Input Function...")
        
# ========== FINAL MESSAGE ==========
print("\n" + "="*50)
AI_response = "Congratulations! You've completed the Python basics tutorial. You learned what you wanted!"
print(AI_response)
print("Keep practicing to enhance your skills. 🥷")
print("="*50)