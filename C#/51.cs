using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = @"c:\users\syed.gardezi\documents\visual studio 2015\Projects\AdventOfCode\AdventOfCode\input\50.txt";

            List<Int32> listOfJumps = new List<int>();

            // Open the text file using a stream reader.
            using (StreamReader sr = new StreamReader(path))
            {
                while (sr.Peek() >= 0)
                {
                    // Read the stream to a string, and write the string to the console.
                    String line = sr.ReadLine().Trim();
                    listOfJumps.Add(Int32.Parse(line));
                        
                }
            }

            

            int jump = 0;
            int count = 0;            
            
            while (jump<listOfJumps.Count) {

                var oldjump = jump;
                jump = oldjump + listOfJumps[oldjump];

                if (listOfJumps[oldjump] >= 3)
                {
                    listOfJumps[oldjump] = listOfJumps[oldjump] - 1;
                }
                else {
                    listOfJumps[oldjump] = listOfJumps[oldjump] + 1;
                }
                count++;
          
            }
            
            Console.WriteLine("Count:"+count);




        }
    }
}
