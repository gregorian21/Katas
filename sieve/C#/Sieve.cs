using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Katas.Sieve {

    public class Sieve {
        public static void Main(string [] args) {
            var maxNum = 0L;

            //Preconditions check
            if (args.Length != 1 || (!(Int64.TryParse(args[0], out maxNum) && maxNum > 0))) {
                Console.WriteLine("Sieve of Eratosthenes - Prints out Prime numbers upto a specified maximum number.");
                Console.WriteLine("Usage:\nSieve.exe max_num (where max_num is a positive integer)");
                System.Environment.Exit(1);
            }

            Console.WriteLine("Primes from 1 to {0}:", maxNum);
            var numbers =  new bool[maxNum+1];

            for (int nextPrime = 2; nextPrime < numbers.Length; nextPrime++) {
                if (numbers[nextPrime]) {
                    continue;
                }

                Console.WriteLine(nextPrime);

                for (int nextComposite = 2 * nextPrime; nextComposite < numbers.Length; nextComposite += nextPrime) {
                    numbers[nextComposite] = true;
                }
            }
        }
    }
}
