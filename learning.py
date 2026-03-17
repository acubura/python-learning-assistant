# Assistant introducing himself:
name = "Python Teaching Assistant"
version = "1.0.2"
category = "Preview"
Description = "An Assistant developed to guide you with Python programming and learning."

def introduce():
    return f"Hello! I am {name}, version {version}, category, {category}. \n{Description}"

print(introduce())

# ========== SMART INPUT VALIDATION FUNCTIONS ==========

# ----- RESPONSE CATEGORIES (Constants for better readability) -----
YES_RESPONSES = ['yes', 'y', 'teach me this topic', 'i want to learn this topic',
                 'wanted to learn more', 'of course! Lets learn this new topic', 'yeah! Teach me man']

NO_RESPONSES = ['no', 'n', 'move on to next topic', 'skip', 'skip the topic', 'I dont have plans to learn this topic',
                'nah! I am not going to continue further', 'I am fine, dont want to learn today', 'I dont want to learn anything']

EXIT_RESPONSES = ['exit', 'e', 'exit the session', 'i want to exit', 
                  'nah! I dont want to study', 'nuh uh! No more, I am quiting', 'I am taking a relaxing break']

YES_EXAMPLES_RESPONSES = ['yes', 'y', 'show me examples', 'i want to see examples', 'give me some examples',
                          'of course! I want to see the example', 'yeah! Show me more examples', 'OK! I want to see more examples']

NO_EXAMPLES_RESPONSES = ['no', 'n', 'skip examples', 'no examples', 'skip showing examples', 'skip this particular example',
                         'nah! I dont want to see examples', 'nuh uh! I am fine without examples', 'I am good, dont show me examples']

YES_QUESTION_RESPONSES = [
    'yes', 'y', 
    'i have a question', 'ask a question', 'i want to ask a question',
    'can you teach', 'can you help me', 'i need help', 
    'i wanted to ask you something', 'yeah! can you help me', 
    'yeah! I have a question'
]

NO_QUESTION_RESPONSES = [
    'no', 'n',
    'no questions', 'i do not have a question', 'skip questions',
    'no! I do not have a question', 'nah! I do not want to ask a question',
    'nuh ! I do not have any questions', 'nuh uh! I do not want to ask anything'
]

EXIT_QUESTION_RESPONSES = [
    'exit', 'e', 'exit the session', 'i want to exit', 'i want to leave',
    'Nuh uh! I want to exit', 'nah! I want to exit', 'no! I want to exit',
    'i want to leave now', 'Nah! I am fine',
    'sorry! But I do not want to learn anything', 'i am good for now'
]

SIMPLE_RESPONSES = ['yes', 'y', 'no', 'n', 'ok', 'okay', 'exit', 'e']

QUESTION_WORDS = [
    'what', 'how', 'why', 'when', 'where', 'who', 'which', 
    'can', 'is', 'are', 'do', 'does', 'should', 'could', 'would', 'will'
]

PYTHON_TERMS = [
    'python', 'function', 'variable', 'hello world', 'relational operator',
    'assignment operator', 'logical operator', 'type conversion', 'input function',
    'comments', 'strings', 'programming', 'coding'
]

# ----- Global Input Validation Functions -----

def get_global_valid_input(prompt):
    """Get and validate user input for yes/no/exit"""
    valid_options = YES_RESPONSES + NO_RESPONSES + EXIT_RESPONSES
    
    while True:
        user_input = input(prompt).strip().lower()
        
        # ----- EMPTY INPUT CHECK -----
        if not user_input:
            print("⚠️  Please enter a valid response (yes/no/exit)")
            continue
        
        # ----- EXACT MATCHES FIRST -----
        if user_input in valid_options:
            if user_input in YES_RESPONSES:
                return 'yes'
            elif user_input in NO_RESPONSES:
                return 'no'
            elif user_input in EXIT_RESPONSES:
                return 'exit'
            else:
                return user_input
        
        # ----- PARTIAL MATCHES -----
        if user_input.startswith('y'):
            return 'yes'
        elif user_input.startswith('n'):
            return 'no'
        elif user_input.startswith('e'):
            return 'exit'
        elif user_input.startswith('s'):
            return 'no'  # skip
        elif 'teach' in user_input or 'learn' in user_input:
            return 'yes'
        
        print("⚠️  Please enter a valid response (yes/no/exit)")

# ----- Global Question-Specific Input Validation Function -----        

def get_global_user_question_valid_input(prompt):
    """Get and validate user input for questions"""
    while True:
        user_input = input(prompt).strip().lower()
        
        # ----- EMPTY INPUT CHECK -----
        if not user_input:
            print("⚠️  Please enter a valid response (yes/no/exit)")
            continue
        
        # ----- EXACT MATCHES -----
        if user_input in YES_QUESTION_RESPONSES:
            return 'yes'
        elif user_input in NO_QUESTION_RESPONSES:
            return 'no'
        elif user_input in EXIT_QUESTION_RESPONSES:
            return 'exit'
        
        # ----- PARTIAL MATCHES -----
        if user_input.startswith('y'):
            return 'yes'
        elif user_input.startswith('n'):
            return 'no'
        elif user_input.startswith('e'):
            return 'exit'
        elif 'question' in user_input or 'ask' in user_input:
            return 'yes'
        elif 'skip' in user_input or 'nah' in user_input or 'nuh' in user_input:
            return 'no'
        elif 'leave' in user_input or 'exit' in user_input:
            return 'exit'
        
        print("⚠️  Please enter a valid response (yes/no/exit)")

#  ----- Global Menu Choice Functions -----

def get_global_menu_choice(prompt, min_val=1, max_val=10):
    """Get and validate user input for menu choice"""
    while True:
        choice = input(prompt).strip().lower()
        
        # ----- EXIT CHECK -----
        if choice == 'exit':
            return 'exit'
        
        # ----- EMPTY INPUT CHECK -----
        if not choice:
            print(f"⚠️  Please enter a number between {min_val} and {max_val}, or 'exit'")
            continue

        # ----- VALID NUMBER CHECK -----
        if choice.isdigit() and min_val <= int(choice) <= max_val:
            return choice

        print(f"⚠️  Please enter a number between {min_val} and {max_val}, or 'exit'")

# ----- Global Examples-Specific Input Validation Function -----        

def get_global_examples_valid_input(prompt):
    """Get and validate user input for examples"""
    while True:
        user_input = input(prompt).strip().lower()
        
        # ----- EMPTY INPUT CHECK -----
        if not user_input:
            print("⚠️  Please enter a valid response (yes/no)")
            continue
        
        # ----- EXACT MATCHES -----
        if user_input in YES_EXAMPLES_RESPONSES:
            return 'yes'
        elif user_input in NO_EXAMPLES_RESPONSES:
            return 'no'
        
        # ----- PARTIAL MATCHES -----
        if user_input.startswith('y'):
            return 'yes'
        elif user_input.startswith('n'):
            return 'no'
        elif 'example' in user_input or 'show' in user_input:
            return 'yes'
        elif 'skip' in user_input:
            return 'no'
        
        print("⚠️  Please enter a valid response (yes/no)")

# ----- Global Question Content Validation Function -----       

def get_global_question_content_input(prompt):
    """Get and validate the actual question content (not yes/no/exit)"""
    
    # ----- HELPER FUNCTIONS -----
    def is_simple_response(text):
        """Check if input is just yes/no/exit"""
        return text in SIMPLE_RESPONSES
    
    def is_full_question(text):
        """Check if input is a complete question (has enough words)"""
        words = text.split()
        
        # Any question with at least 4 words is likely complete
        # "Can you teach me?" = 4 words
        # "How to learn Python?" = 4 words
        # "What is a variable?" = 4 words
        return len(words) >= 4
    
    def print_helpful_feedback():
        """Print helpful examples"""
        print("\n❌ Please ask a complete question (at least 4 words).")
        print("\n📝 Examples:")
        print("   • 'Can you teach me Python?'")
        print("   • 'How do I learn variables?'")
        print("   • 'What is a function?'")
        print("   • 'Can you explain loops?'")
        print()
    
    # ----- MAIN VALIDATION LOOP -----
    while True:
        question = input(prompt).strip()
        
        # ----- EMPTY INPUT CHECK -----
        if not question:
            print("⚠️  Please enter a valid question.")
            continue
        
        question_lower = question.lower()
        
        # ----- SIMPLE RESPONSE CHECK -----
        if is_simple_response(question_lower):
            print("⚠️  Please ask an actual Python question, not just 'yes' or 'no'.")
            continue
        
        # ----- CHECK IF IT'S A FULL QUESTION -----
        if is_full_question(question):
            return question
        
        # ----- HELPFUL FEEDBACK -----
        print_helpful_feedback()

# ========== Global Seperator for better readability ==========
def print_global_separator():
    global_separator = "\n" + "="*50
    print(global_separator)

# ========== START OF THE CONVERSATION ==========
print("\nHow can I assist you with Python programming today?")

# Ask if user has a specific question
user_question = get_global_user_question_valid_input("\n🔹 Do you have any specific questions about Python? (yes/no/exit): ")

# Handle user's question if they have one
user_python_question = ""
if user_question == 'yes':
    print("\n🔹 Please ask your Python question:")
    user_python_question = get_global_question_content_input("💬 Your Question: ") 
    print(f"\n🤖 Thank you for your question: '{user_python_question}'")
    
    user_input = get_global_valid_input("\n🔹 Would you like to learn Python topics? (yes/no/exit): ")
    
    # If user chooses 'exit' after asking question, end the session
    if user_input == 'exit':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        exit()         
    # If user chooses 'no' after asking question, proceed to topics menu
    elif user_input == 'no':
        print("\n🔹 Okay, we will do it later")
        exit()    

elif user_question == 'no':
    print("\n🔹 No problem! We can proceed to Python topics anytime you want.")
    user_input = get_global_valid_input("\n🔹 Would you like to learn Python topics after break now? (yes/no/exit): ")
    
    if user_input == 'exit':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        exit()
    elif user_input == 'no':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        exit()
    # If user says 'yes', continue to topics menu
    
elif user_question == 'exit':
    print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
    exit()

# ========= MAIN TOPICS LOOP ==========
while True:
    # ========= TOPICS MENU ==========        
    print_global_separator()
    Assistant_Response = "I can teach you Python basics! Here are the available topics:\n" \
                         "📚 Topics Menu:\n" \
                         "1. Hello World\n" \
                         "2. Functions\n" \
                         "3. Variables\n" \
                         "4. Relational operators\n" \
                         "5. Assignment operators\n" \
                         "6. Logical operators\n" \
                         "7. Type conversion\n" \
                         "8. Input function\n" \
                         "9. Comments in Python\n" \
                         "10. Strings in Python\n"

    print(Assistant_Response)
    print_global_separator()

    # Get topic choice
    Assistant_Ask = "\n🔹 Which topic would you like to start with? (1-10/exit): "
    topic_choice = get_global_menu_choice(Assistant_Ask, 1, 10)

    if topic_choice == 'exit':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        break

    # Map topic numbers to names
    topics = {
        '1': 'Hello World',
        '2': 'Functions',
        '3': 'Variables',
        '4': 'Relational operators',
        '5': 'Assignment operators',
        '6': 'Logical operators',
        '7': 'Type conversion',
        '8': 'Input function',
        '9': 'Comments in Python',
        '10': 'Strings in Python'
    }

    selected_topic = topics[topic_choice]
    print(f"\n🎯 Excellent choice! You selected: {selected_topic}")

    # Ask if they want to learn this topic
    learn_topic = get_global_valid_input(f"\n🔹 Would you like me to teach you about {selected_topic}? (yes/no/exit): ")

    if learn_topic == 'exit':
        print("\n👋 Goodbye! Come back whenever you need me")
        break
    elif learn_topic == 'no':
        print(f"\n🔹 Okay, skipping {selected_topic}.")
        print("\n🔹 You can select another topic from the menu.")
        continue
    
    print(f"\n📖 Teaching {selected_topic}...")
    
    # TEACH THE SELECTED TOPIC BASED ON USER'S CHOICE
    if selected_topic == 'Hello World':
        # ========== TOPIC 1: HELLO WORLD ==========
        print_global_separator()
        print("1. Hello World Example:")
        print('   print("Hello, World!")')
        
        def explain_hello_world():
            print_global_separator()
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
            
            see_example = get_global_examples_valid_input("\nWant to see the code breakdown? (yes/no): ")
            if see_example == 'yes':
                print("\n📝 CODE EXAMPLE:")
                print('   print("Hello, World!")')
                print("   ↑         ↑")
                print("   Command   Message")
            else:
                print("Skipping code breakdown...")
            
            print_global_separator()
            print("You can try it whenever you want! Just type: print('Your Name Here')")
            print_global_separator()
        
        explain_hello_world()
        
        Assistant_Response = "Awesome! You've learned how to print text in Python."
        print(Assistant_Response)
    
    elif selected_topic == 'Functions':
        # ========== TOPIC 2: FUNCTIONS ==========
        print_global_separator()
        print("2. Functions in Python:")
        
        def explain_functions():
            print("\n   📦 What are functions?")
            print("\n🤖 FUNCTIONS = YOUR CODING ASSISTANTS")
            print_global_separator()
            
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
            
            see_example = get_global_examples_valid_input("\nWant to see a function example? (yes/no): ")
            if see_example == 'yes':
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
        
        Assistant_Response = "Awesome! You've learned about functions and how to create and use them."
        print(Assistant_Response)
    
    elif selected_topic == 'Variables':
        # ========== TOPIC 3: VARIABLES ==========
        print_global_separator()
        print("3. Variables in Python:")
        
        def explain_variables():
            print("\n   🏷️ What are variables?")
            print("\n📦 VARIABLES: YOUR CODE'S STORAGE BOXES")
            print_global_separator()
            
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
            
            see_examples = get_global_examples_valid_input("\nWant to see variable examples? (yes/no): ")
            if see_examples == 'yes':
                print("\n📝 REAL EXAMPLE:")
                print("   name = 'Muhammad Qasim'   ← STRING variable")
                print("   age = 18                   ← INTEGER variable")
                print("   score = 95.5               ← FLOAT variable")
                print("   passed = True              ← BOOLEAN variable")
            else:
                print("Skipping examples...")
            
            print_global_separator()
            print("ALWAYS REMEMBER VARIABLES SO, YOU DON'T HAVE TO!")
            print_global_separator()
        
        explain_variables()
        
        Assistant_Response = "Great job! You've learned about variables and their types."
        print(Assistant_Response)
    
    elif selected_topic == 'Relational operators':
        # ========== TOPIC 4: RELATIONAL OPERATORS ==========
        print_global_separator()
        print("4. Relational Operators in Python:")
        
        def explain_relational_operators():
            print("\n   🔍 What are relational operators?")
            print("\n🔍 RELATIONAL OPERATORS: CODE'S COMPARISON TOOLS")
            print_global_separator()
            
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
            
            see_examples = get_global_examples_valid_input("\nWant to see practical examples? (yes/no): ")
            if see_examples == 'yes':
                print("\n📝 PRACTICAL EXAMPLES:")
                print("   age = 18")
                print("   can_vote = age >= 18      # True ✓")
                print("   is_minor = age < 18       # False ✗")
                print("   is_teenager = age >= 13 and age <= 19  # True ✓")
            else:
                print("Skipping examples...")
            
            print_global_separator()
            print("EVERY 'IF' DECISION USES THESE OPERATORS!")
            print_global_separator()
            
            print_global_separator()
            Assistant_Response = "Of course! Relational operators compare two values and return True or False based on the comparison."
            print(Assistant_Response)
            print("\n   💡 Explanation:")
            print("   - Relational operators compare two values")
            print("   - Useful in decision-making and control flow")
        
        explain_relational_operators()
    
    elif selected_topic == 'Assignment operators':
        # ========= TOPIC 5: Assignment Operators ==========
        print_global_separator()
        print("5. Assignment Operators in Python:")
        
        def explain_assignment_operators():
            print("\n   📝 What are assignment operators?")
            print("\n📝 ASSIGNMENT OPERATORS: CODE'S VALUE ASSIGNERS")
            print_global_separator()
            
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
            
            print_global_separator()
            print("Assignment operators make your code SHORTER!")
            print_global_separator()
        
        explain_assignment_operators()
        
        print("\nGreat! You learned about assignment operators!")
    
    elif selected_topic == 'Logical operators':
        # ========= TOPIC 6: LOGICAL OPERATORS ==========
        print_global_separator()
        print("6. Logical Operators in Python:")
        
        def explain_logical_operators():
            print("\n   🤔 What are logical operators?")
            print("\n🤔 LOGICAL OPERATORS: CODE'S THINKING TOOLS")
            print_global_separator()
            
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
            
            print_global_separator()
            print("Logical operators help your code THINK SMARTER!")
            print_global_separator()
        
        explain_logical_operators()
        
        Assistant_Response = "Great! You learned about logical operators!"
        print(Assistant_Response)
    
    elif selected_topic == 'Type conversion':
        # ==== TOPIC 7: TYPE CONVERSION ===========
        print_global_separator()
        print("7. Type Conversion in Python:")
        
        def explain_type_conversion():
            print("\n   🔄 What is type conversion?")
            print("\n🔄 TYPE CONVERSION: CHANGING DATA TYPES")
            print_global_separator()
            
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
            
            print_global_separator()
            print("Implicit = Python decides, Explicit = YOU decide!")
            print_global_separator()
        
        explain_type_conversion()
        
        Assistant_Response = "Great! You learned about type conversion!"
        print(Assistant_Response)
    
    elif selected_topic == 'Input function':
        # ========= TOPIC 8: INPUT FUNCTION ==========
        print_global_separator()
        print("8. Input Function in Python:")
        
        def explain_input_function():
            print("\n   🖊️ What is the input function?")
            print("\n🖊️ INPUT FUNCTION: GETTING USER DATA")
            print_global_separator()
            
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
            
            print_global_separator()
            print("Input function makes your program INTERACTIVE!")
            print_global_separator()
        
        explain_input_function()
        
        Assistant_Response = "Great! You learned about the input function!"
        print(Assistant_Response)
    
    elif selected_topic == 'Comments in Python':
        # ======== TOPIC 9: COMMENTS IN PYTHON ==========
        print_global_separator()
        print("9. Comments in Python:")
        
        def explain_comments():
            print("\n   📝 What are comments?")
            print("\n📝 COMMENTS: EXPLAINING YOUR CODE")
            print_global_separator()
            
            print("""
            🎯 WHAT ARE THEY?
            Comments are notes in your code that are ignored by Python.
            They help explain what your code does.
            
            🔧 HOW TO WRITE THEM:
            # This is a single-line comment
            # You can write anything here
            
            ''' This is a multi-line comment
            You can write multiple lines here
            Python will ignore all of them '''
            
            💡 EXAMPLES:
            # This program calculates the area of a rectangle
            length = 10
            width = 5
            area = length * width  # Calculate area
            
            🔑 TIPS:
            • Use comments to explain complex logic
            • Comment out code you want to test later
            • Keep comments up-to-date with your code
            
            ⚠️ COMMON MISTAKES:
            Don't over-comment simple lines!
            """)
            
            print_global_separator()
            print("Comments help OTHERS (and FUTURE YOU) understand your code!")
            print_global_separator()
        
        explain_comments()

        Assistant_Response = "Great! You learned about comments!"
        print(Assistant_Response)
    
    
    elif selected_topic == 'Input function':
        # ========= TOPIC 8: INPUT FUNCTION ==========
        print_global_separator()
        print("8. Input Function in Python:")
        
        def explain_input_function():
            print("\n   🖊️ What is the input function?")
            print("\n🖊️ INPUT FUNCTION: GETTING USER DATA")
            print_global_separator()
            
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
            
            print_global_separator()
            print("Input function makes your program INTERACTIVE!")
            print_global_separator()
        
        explain_input_function()
        
        Assistant_Response = "Great! You learned about the input function!"
        print(Assistant_Response)
    
    elif selected_topic == 'Comments in Python':
        # ======== TOPIC 9: COMMENTS IN PYTHON ==========
        print_global_separator()
        print("9. Comments in Python:")
        
        def explain_comments():
            print("\n   📝 What are comments?")
            print("\n📝 COMMENTS: EXPLAINING YOUR CODE")
            print_global_separator()
            
            print("""
            🎯 WHAT ARE THEY?
            Comments are notes in your code that are ignored by Python.
            They help explain what your code does.
            
            🔧 HOW TO WRITE THEM:
            # This is a single-line comment
            # You can write anything here
            
            ''' This is a multi-line comment
            You can write multiple lines here
            Python will ignore all of them '''
            
            💡 EXAMPLES:
            # This program calculates the area of a rectangle
            length = 10
            width = 5
            area = length * width  # Calculate area
            
            🔑 TIPS:
            • Use comments to explain complex logic
            • Comment out code you want to test later
            • Keep comments up-to-date with your code
            
            ⚠️ COMMON MISTAKES:
            Don't over-comment simple lines!
            """)
            
            print_global_separator()
            print("Comments help OTHERS (and FUTURE YOU) understand your code!")
            print_global_separator()
        
        explain_comments()

        Assistant_Response = "Great! You learned about comments!"
        print(Assistant_Response)
    
    elif selected_topic == 'Strings in Python':
        # ======== TOPIC 10: STRINGS IN PYTHON ==========
        print_global_separator()
        print("10. Strings in Python:")

        # Define all helper functions FIRST before they are called
        def teach_string_basics():
            """Teach string basics"""
            print_global_separator()
            print("📘 PART 1: String Basics & Creation")
            print_global_separator()
            
            print("""
        📝 BASIC STRING EXAMPLES:
        name = 'Alice'                    # Single quotes
        greeting = "Hello, World!"        # Double quotes
        paragraph = '''This is a           # Multi-line string
        multi-line string that
        spans several lines.'''
        
        🎯 KEY POINTS:
        • Strings can use single, double, or triple quotes
        • Triple quotes allow multi-line strings
        • Strings are IMMUTABLE (cannot be modified)
        • Use len() to get string length
            """)
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                text = "Python Programming"
                print(f"\n   text = \"{text}\"")
                print(f"   Length: {len(text)} characters")
                print(f"   Type: {type(text)}")
                print(f"   Uppercase: {text.upper()}")
                print(f"   Lowercase: {text.lower()}")

        def teach_string_indexing():
            """Teach string indexing and slicing"""
            print_global_separator()
            print("📘 PART 2: Indexing & Slicing")
            print_global_separator()
            
            print("""
        🔤 INDEXING (Accessing individual characters):
        Python uses ZERO-BASED indexing
        
        Positions:   0   1   2   3   4   5
        String:     P   y   t   h   o   n
        Index:      0   1   2   3   4   5
        Negative:  -6  -5  -4  -3  -2  -1
        
        🔪 SLICING (Getting parts of string):
        Syntax: string[start:end:step]
        • start: Starting index (inclusive)
        • end: Ending index (exclusive)
        • step: Jump size
            """)
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                text = "PythonProgramming"
                print(f"\n   text = \"{text}\"")
                print(f"   text[0] = '{text[0]}'           # First character")
                print(f"   text[-1] = '{text[-1]}'         # Last character")
                print(f"   text[0:6] = \"{text[0:6]}\"     # Characters 0 to 5")
                print(f"   text[6:] = \"{text[6:]}\"       # From index 6 to end")
                print(f"   text[::-1] = \"{text[::-1]}\"   # Reversed string")

        def teach_string_operations():
            """Teach string operations"""
            print_global_separator()
            print("📘 PART 3: String Operations")
            print_global_separator()
            
            print("""
        ⚙️ CONCATENATION (+): Joining strings
        str1 = "Hello"
        str2 = "World"
        result = str1 + " " + str2  # "Hello World"
        
        🔁 REPLICATION (*): Repeating strings
        laugh = "ha" * 3  # "hahaha"
        separator = "-" * 20  # "--------------------"
        
        🔍 MEMBERSHIP (in/not in): Check substring
        text = "Python is awesome"
        has_python = "Python" in text  # True
        has_java = "Java" not in text  # True
            """)
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                str1 = "Hello"
                str2 = "World"
                print(f"\n   str1 = \"{str1}\"")
                print(f"   str2 = \"{str2}\"")
                print(f"   Concatenation: str1 + ' ' + str2 = \"{str1 + ' ' + str2}\"")
                print(f"   Replication: 'ha' * 3 = \"{'ha' * 3}\"")
                print(f"   Membership: 'Python' in 'Python Programming' = {'Python' in 'Python Programming'}")

        def teach_string_methods():
            """Teach string methods"""
            print_global_separator()
            print("📘 PART 4: String Methods")
            print_global_separator()
            
            print("""
        🛠️ COMMON STRING METHODS:
        
        ✂️ TRIMMING:
        spaced = "   Hello   "
        stripped = spaced.strip()      # "Hello"
        left_stripped = spaced.lstrip() # "Hello   "
        right_stripped = spaced.rstrip() # "   Hello"
        
        🔎 SEARCHING:
        text = "Python Programming"
        find_pro = text.find("Pro")    # 7 (index where found)
        count_n = text.count("n")      # 2 (count of 'n')
        
        🔀 SPLITTING & JOINING:
        sentence = "Python,Java,C++"
        languages = sentence.split(",") # ["Python", "Java", "C++"]
        new_sentence = "-".join(languages) # "Python-Java-C++"
        
        🔧 REPLACING:
        text = "I love Java"
        new_text = text.replace("Java", "Python") # "I love Python"
            """)
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                text = "   Python Programming   "
                print(f"\n   text = \"{text}\"")
                print(f"   strip(): \"{text.strip()}\"")
                print(f"   upper(): \"{text.upper()}\"")
                print(f"   lower(): \"{text.lower()}\"")
                print(f"   replace('Python', 'Java'): \"{text.replace('Python', 'Java')}\"")
                print(f"   split(): {text.strip().split()}")

        def teach_string_formatting():
            """Teach string formatting"""
            print_global_separator()
            print("📘 PART 5: String Formatting")
            print_global_separator()
            
            print("""
        🎨 STRING FORMATTING METHODS:
        
        1️⃣ f-strings (Python 3.6+): RECOMMENDED!
        name = "Alice"
        age = 25
        message = f"My name is {name} and I am {age} years old."
        # Result: "My name is Alice and I am 25 years old."
        
        2️⃣ format() method:
        message = "My name is {} and I am {} years old.".format(name, age)
        
        3️⃣ % formatting (old style):
        message = "My name is %s and I am %d years old." % (name, age)
        
        🎯 NUMBER FORMATTING:
        price = 49.9999
        formatted = f"Price: ${price:.2f}"  # "Price: $50.00"
        
        pi = 3.1415926535
        formatted_pi = f"Pi: {pi:.4f}"     # "Pi: 3.1416"
            """)
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                name = "Alice"
                age = 25
                price = 49.9999
                print(f"\n   name = \"{name}\", age = {age}, price = {price}")
                print(f"   f-string: f'Name: {name}, Age: {age}' = \"{f'Name: {name}, Age: {age}'}\"")
                print("   format(): 'Name: {}, Age: {}' = \"" + 'Name: {}, Age: {}'.format(name, age) + "\"")
                print(f"   Number formatting: f'Price: ${price:.2f}' = \"{f'Price: ${price:.2f}'}\"")

        def teach_string_errors():
            """Teach common string errors and best practices"""
            print_global_separator()
            print("📘 PART 6: Common Errors & Best Practices")
            print_global_separator()
            
            print("""
        ⚠️ COMMON STRING ERRORS:
        
        1️⃣ IMMUTABILITY ERROR:
        text = "Hello"
        text[0] = "J"  # ❌ ERROR! Strings are immutable
        
        Correct approach:
        text = "J" + text[1:]  # ✅ Creates new string "Jello"
        
        2️⃣ ESCAPE CHARACTERS:
        # Wrong: path = "C:\\new folder"  # \\n is newline!
        # Right: path = "C:\\\\new folder" or r"C:\\new folder"
        
        Common escape sequences:
        \\n → New line
        \\t → Tab
        \\\\ → Backslash
        \\" → Double quote
        \\' → Single quote
        
        3️⃣ MIXING DATA TYPES:
        age = 25
        # Wrong: message = "I am " + age + " years old"
        # Right: message = "I am " + str(age) + " years old"
        # Better: message = f"I am {age} years old"
        
        💡 BEST PRACTICES:
        1. Use f-strings for formatting (Python 3.6+)
        2. Remember strings are IMMUTABLE
        3. Use .strip() to clean user input
        4. Prefer .join() for concatenating many strings
        5. Use raw strings (r"") for paths and regex
            """)

        def teach_all_string_topics():
            """Teach all string topics in sequence"""
            teach_string_basics()
            teach_string_indexing()
            teach_string_operations()
            teach_string_methods()
            teach_string_formatting()
            teach_string_errors()

        def explain_strings():
            """Comprehensive guide to Python strings"""
            print("\n   💬 What are strings?")
            print("\n💬 STRINGS: TEXT DATA IN PYTHON")
            print_global_separator()
            
            print("""
        🎯 WHAT ARE STRINGS?
        Strings are SEQUENCES OF CHARACTERS used to store and manipulate text.
        In Python, strings are IMMUTABLE (cannot be changed once created).
        
        🔧 CREATING STRINGS:
        • Single quotes: 'Hello'
        • Double quotes: "World"
        • Triple quotes: '''Multi-line strings''' or \"\"\"Also multi-line\"\"\"
            """)
            
            # Track which topics have been learned
            topics_learned = []
            
            while True:
                # Display menu
                print("\n📚 STRINGS TOPIC MENU:")
                print("   1. String Basics & Creation")
                print("   2. Indexing & Slicing")
                print("   3. String Operations")
                print("   4. String Methods")
                print("   5. String Formatting")
                print("   6. Common Errors & Best Practices")
                print("   7. All topics (Complete guide)")
                print("   8. I'm done with strings (exit strings)")
                
                topic_choice = get_global_menu_choice("\n🔹 Which string topic would you like to learn? (1-8/exit): ", 1, 8)
                
                # Handle exit
                if topic_choice == 'exit':
                    print("\n👋 Session ended. Goodbye!")
                    exit()
                
                # Handle return to main menu
                if topic_choice == '8':
                    print("\n✅ Exiting strings section...")
                    break
                
                # Check if topic was already learned (skip for "All topics")
                if topic_choice in topics_learned and topic_choice != '7':
                    review = get_global_valid_input(f"\n🔹 You've already learned topic {topic_choice}. Review it again? (yes/no): ")
                    if review == 'no':
                        continue
                
                # Handle "All topics" selection
                if topic_choice == '7':
                    teach_all_string_topics()
                    topics_learned = ['1', '2', '3', '4', '5', '6']
                    print_global_separator()
                    print("🎉 COMPLETE STRINGS GUIDE FINISHED!")
                    print_global_separator()
                    break
                
                # Teach individual topic based on choice
                if topic_choice == '1':
                    teach_string_basics()
                    if '1' not in topics_learned:
                        topics_learned.append('1')
                
                elif topic_choice == '2':
                    teach_string_indexing()
                    if '2' not in topics_learned:
                        topics_learned.append('2')
                
                elif topic_choice == '3':
                    teach_string_operations()
                    if '3' not in topics_learned:
                        topics_learned.append('3')
                
                elif topic_choice == '4':
                    teach_string_methods()
                    if '4' not in topics_learned:
                        topics_learned.append('4')
                
                elif topic_choice == '5':
                    teach_string_formatting()
                    if '5' not in topics_learned:
                        topics_learned.append('5')
                
                elif topic_choice == '6':
                    teach_string_errors()
                    if '6' not in topics_learned:
                        topics_learned.append('6')
                
                # Ask if user wants to continue with strings
                continue_learning = get_global_valid_input("\n🔹 Want to learn another string topic? (yes/no): ")
                if continue_learning == 'no':
                    print("\n✅ Exiting strings section...")
                    break

        # Now call explain_strings()
        explain_strings()

        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with a string example? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE STRING PRACTICE")
            print_global_separator()
            
            user_text = input("Enter a text to practice with: ").strip()
            
            if user_text:
                print(f"\n📊 ANALYSIS OF YOUR TEXT: \"{user_text}\"")
                print(f"   Length: {len(user_text)} characters")
                print(f"   First character: '{user_text[0]}'")
                print(f"   Last character: '{user_text[-1]}'")
                print(f"   Uppercase: {user_text.upper()}")
                print(f"   Lowercase: {user_text.lower()}")
                print(f"   Title case: {user_text.title()}")
                
                if len(user_text) >= 3:
                    print(f"   First 3 characters: '{user_text[:3]}'")
                    print(f"   Last 3 characters: '{user_text[-3:]}'")
                    print(f"   Middle section: '{user_text[1:-1]}'")
                
                vowels = "aeiouAEIOU"
                vowel_count = sum(1 for char in user_text if char in vowels)
                print(f"   Vowel count: {vowel_count}")
                
                print("\n✅ Practice complete! You've applied string operations!")
            else:
                print("⚠️  No text entered for practice.")

        Assistant_Response = "Excellent! You've learned comprehensive string handling in Python!"
        print(Assistant_Response)

        # Ask if user wants to learn another topic
        print_global_separator()
        learn_more = get_global_valid_input("\n🔹 Would you like to learn another topic? (yes/no/exit): ")

        if learn_more == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            exit()
        elif learn_more == 'no':
            break
        # If yes, the loop continues

# ========== FINAL MESSAGE ==========
print_global_separator()
Assistant_Response = "Congratulations! You've completed the Python basics tutorial 🐍 You learned what you wanted!"
print(Assistant_Response)
print("Keep practicing to enhance your skills. 🥷")
print_global_separator()
