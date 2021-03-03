# NGS_coverage_report
The find_genes.py Python script extends the coverage report produced by the sambamaba tool pipeline by outputting a list of genes that have less than 100% at 30x coverage.
The URL of the incomplete sambamba output is the input of the find_genes.py script. The output file of the script is named Genes_with_less_than_100%_30x_coverage.csv. Below are instructions to run the script in a mac terminal.

To run...
# install libraries in your terminal
pip3 install pandas

pip3 install requests
# clone the GitHub repositiory 
git clone https://github.com/hasmitapatel18/NGS_coverage_report.git
# change directories to the NGS_coverage_report folder
cd NGS_coverage_report
# run the find_genes.py script
python3 find_genes.py

