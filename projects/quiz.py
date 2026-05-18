while True:
    print("-----Welcome to Quiz-----")

    print("Select the category you want to play")
    print("1 → General Knowledge questions")
    print("2 → Sports questions")
    print("3 → Python questions")
    print("4 → Exit:")
   
    choice=int(input("Enter your choice:"))

    score = 0

    match choice:
    
        case 1: 

           print("\n Here Your General Knowledge Questions")
           print("\n Q1. Which planet is called the Red Planet?")
           
           print("a → Earth")
           print("b → Mars")
           print("c → Venus")
           print("d → Jupiter")
          
           option =input("\nEnter your option ")
           match option:

               case "b": 
                   print("✅ You are correct!")
                   score +=1

               case _:
                   print("❌ You are wrong, the correct ans is b → Mars")

           print("\n------------------------------------")

           print("\n Q2. Who is known as the Father of Computer? ")
            
           print("a → Charles Babbage") 
           print("b → Newton ")
           print("c → Einstein")
           print("d → Bill Gates")

           option =input("\nEnter your option ")
           match option:

               case "a": 
                   print("✅ You are correct!")
                   score +=1

               case _:
                   print("❌ You are wrong, the correct ans is a → Charles Babbage")

           print("\n------------------------------------")

           print("\nQ3. What is the capital of India?")

           print("a → Mumbai")
           print("b → Delhi")
           print("c → Pune")
           print("d → Kolkata")

           option = input("\nEnter your option: ")

           match option:

              case "b":
                   print("✅ You are correct!")
                   score += 1

              case _:
                   print("❌ Wrong! Correct answer is b → Delhi")

        case 2:
            print("\n Here Your Sports Related Questions")
            print("\n Q1. Which country won the Cricket World Cup 2011?")

            print("a → Australia")
            print("b → England")
            print("c → India")
            print("d → Pakistan")

            option = input("\nEnter your option ")

            match option:

              case "c": 
                   print("✅ You are correct!")
                   score +=1

              case _:
                   print("❌ You are wrong, the correct ans is c → India")

            print("\n------------------------------------")

            print("\n Q2. Which sport is played with a shuttlecock?")

            print("a → Tennis")
            print("b → Cricket")
            print("c → Hockey")
            print("d → Badminton")

            option = input("\nEnter your option ")

            match option:

              case "d": 
                   print("✅ You are correct!")
                   score +=1

              case _:
                   print("❌ You are wrong, the correct ans is d → Badminton")

            print("\n------------------------------------")

             
            print("\nQ3. How many players are there in a cricket team?")

            print("a → 9")
            print("b → 10")
            print("c → 11")
            print("d → 12")

            option = input("\nEnter your option: ")

            match option:

               case "c":
                   print("✅ You are correct!")
                   score += 1

               case _:
                   print("❌ Wrong! Correct answer is c → 11")

        case 3:
            print("\n Here Your Python Related Questions")
            print("\n Q1. Which loop is used when number of iterations is known?")

            print("a → while")
            print("b → do-while")
            print("c → for")
            print("d → nested")

            option = input("\nEnter your option ")

            match option:

              case "c": 
                   print("✅ You are correct!")
                   score +=1

              case _:
                   print("❌ You are wrong, the correct ans is c → for")

            print("\n------------------------------------")

            print("\n Q2. Which keyword is used for decision making?")
 
            print("a → loop")
            print("b → switch")
            print("c → if")
            print("d → def")


            option = input("\nEnter your option ")

            match option:

              case "c": 
                  print("✅You are correct!")
                  score +=1

              case _:
                  print("❌You are wrong, the correct ans is c → if")

            print("\n------------------------------------")

          
            print("\nQ3. Which symbol is used for comments in Python?")

            print("a → //")
            print("b → #")
            print("c → /*")
            print("d → --")

            option = input("\nEnter your option: ")

            match option:

              case "b":
                  print("✅ You are correct!")
                  score += 1

              case _:
                  print("❌ Wrong! Correct answer is b → #")

        case 4:
            print("Exit from quiz")
            break

        case _:
            print("Invalid choice")


    if choice in [1, 2, 3]:
        
        print("\n========== QUIZ RESULT ==========")

        print("Your Score:", score, "/3")

        percentage = (score / 3) * 100
        
        print("Percentage:", percentage, "%")

      

        if score == 3:
            print("🏆 Grade A+ : Excellent Performance!")

        elif score == 2:
            print("👍 Grade B : Good Job!")

        elif score == 1:
            print("🙂 Grade C : Keep Practicing!")

        else:
            print(" Better Luck Next Time!")
 
        print("=================================")

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() == "no":
        print("\n🙏 Thank You For Playing Quiz!")
        break
