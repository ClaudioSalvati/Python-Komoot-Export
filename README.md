# Python-Komoot-Export
Export all tour data and gpx tracks from Komoot via Python and make them available for analysis.

## Motivation
I wanted to download all komoot data to analyse it in Tableau. To avoid downloading all tour manually, I started looking around for ready-to-use scripts for python. 
I came along [Get Komoot tour data without API](https://python.plainenglish.io/get-komoot-tour-data-without-api-143df64e51fa), pointing to [github.com/simplylu/medium_komoot](https://github.com/simplylu/medium_komoot), but I wasn't that happy with it.
So I started adjusting the code and this is the result.

## Limitations
I have limited knowledge of python, so the code will have great potential for optimizatio in terms of simplicity and performance.
The URLs used to extract data from Komoot can be subject to sudden and unannouced changes.

## The result
With the following script, you can export your komoot data in JSON format and store is as CSV, ready to be used for any analysis you have in mind. 
* 01 Get Komoot tour JSON data.py
  * This script will download the full tour track as GPX, as well as some information about the tour as JSON
  * The GPX can be downloaded only if the tour is public. For private tours, you will have to consider other methods to export the data
  * Nevertheless you will have to enter your credentials to export the tours
* 02 Convert Komoot GPX files to CSV.py
  * This script convert the GPX files to CSV format for better handling in Tableau
* 03 Convert Komoot JSON files to CSV.py
  * This script convert the JSON files to CSV format for better handling in Tableau
* 04 Merge CSV files by type (GPX and Tour Info).py
  * This script is needed to merge the many CSV files to one, separating them by data type (GPX and Tour Info)
* 05 Join GPX and Tour Info CSV files.py
  * This script joins the two CSV files of the previous step (04)
  * It is not required for an analysis in Tableau or PowerBi, but can be useful if you use Excel

## Credits
As already mentioned, the original code for the extraction (step 1) comes from [simplylu](https://github.com/simplylu/). The rest is the result of fulfilling my own needs in a simple way.

## Disclaimer
I offer the code as-is and as-available, and I make no representations or warranties of any kind concerning it, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable.
