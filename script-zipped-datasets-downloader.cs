using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace zip_down
{
    static class Program
    {

        static void Main()
        {
            try
            {
                fileExtractor();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }

        }

        static void fileExtractor()
        {
            try
            {
                
                DirectoryInfo d = new DirectoryInfo(@"C:\Users\hp\Desktop\street-hack\zip-files");
                FileInfo[] Files = d.GetFiles();
                
                foreach (FileInfo file in Files)
                {
                    string zipPath = string.Format(@"C:\Users\hp\Desktop\street-hack\zip-files\{0}", file);
                    string extractPath = string.Format(@"C:\Users\hp\Desktop\street-hack\extracted-files\{0}", file);

                    System.IO.Compression.ZipFile.ExtractToDirectory(zipPath, extractPath);
                }

               
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }

        }


        static void fileDownloader()
        {
            WebClient webClient = new WebClient();
            string[] lines = File.ReadAllLines(@"D:\zip-url.txt");
            int count = 0;
            foreach (string line in lines)
            {
                string myurl = line;
                Console.WriteLine(line.Length);
                string file_name = line.Substring(65, 17);

                string file_path = string.Format(@"C:\Users\hp\Desktop\street-hack\zip-files\{0}", file_name);
                webClient.DownloadFile(new Uri(myurl), file_path);

                count++;
            }
        }

    }
}
