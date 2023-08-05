# Python-Komoot-Export
Export all tour data and gpx tracks from Komoot via Python.

## Motivation
I wanted to download all komoot data to analyse it in Tableau. To avoid downloading all tour manually, I started looking around for ready-to-use scripts for python. 
I came along [Get Komoot tour data without API](https://python.plainenglish.io/get-komoot-tour-data-without-api-143df64e51fa), pointing to [github.com/simplylu/medium_komoot](https://github.com/simplylu/medium_komoot), but I wasn't that happy with it.
So I started writing the code with the help of ChatGPT and this is the result

## Limitations
I have limited knowledge of python, so the code will have great potential for optimizatio in terms of simplicity and performance.
The URLs used to extract data from Komoot can be subject to sudden and unannouced changes.

## The result
With the following script, you can export your komoot data in JSON format and store is as CSV, ready to be used for any analysis you have in mind. 
* Get Komoot tour JSON data.py
  * This script will download the full tour track as GPX, as well as some information about the tour as JSON
  * The GPX can be downloaded only if the tour is public. For private tours, you will have to consider other methods to export the data
  * Nevertheless you will have to enter your credentials to export the tours
* Convert Komoot GPX files to CSV.py
  * This scripts convert the GPX files to CSV format for better handling in Tableau
* Convert Komoot JSON files to CSV.py
  * This scripts convert the JSON files to CSV format for better handling in Tableau

## Credits
As already mentioned, the original code for the extraction comes from [simplylu](https://github.com/simplylu/).
