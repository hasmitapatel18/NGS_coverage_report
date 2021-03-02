import pandas as pd
import requests
import io


class Manager():
    
    def __init__(self):
        read_file = ReadFile()
        less_than_30x = LessThan30x(read_file.get_data())
        output = Output(less_than_30x.get_gene_list())
        
        
class ReadFile():
    
    #set url as an instance variable
    url = "https://raw.githubusercontent.com/mokaguys/coverage_test/master/NGS148_34_139558_CB_CMCMD_S33_R1_001.sambamba_output.txt"
    
    def __init__(self):
        self.input = self.read_input_file()
        
    def read_input_file(self):
        download = requests.get(self.url).content
        #read data as CSV, separate by tab and space
        data = pd.read_csv(io.StringIO(download.decode('utf-8')), sep="\t| ", engine='python')
        return data
    
    def get_data(self):
        return self.input

        
class LessThan30x():
    
    def __init__(self, input_df):
        self.input_df = input_df
        less_than_100 = self.find_less_than_100_percent(input_df)
        self.associated_genes = self.find_associated_genes(less_than_100)
    
    def find_less_than_100_percent(self, input_df):
        #return new df with rows that have less than 100% in the percentage30 column 
        less_than_100_df = input_df[input_df['percentage30'] < 100]
        return less_than_100_df
    
    def find_associated_genes(self, less_than_100_df):
        #using sets to find unique genes
        gene_set=set()
        #iterate through the df with less than 100% 30x coverage and select gene symbol column, add to set to find unique genes
        for index, rows in less_than_100_df.iterrows():
            gene = rows['GeneSymbol;Accession']
            gene_set.add(gene)
        gene_list = list(gene_set)
        return gene_list
    
    def get_gene_list(self):
        return self.associated_genes
    
    
class Output():
    
    def __init__(self, gene_list):
        self.gene_list = gene_list
        self.output_df = self.output_df(self.gene_list)
        self.output_csv = self.output_csv(self.output_df)
    
    def output_df(self, gene_list):
        #making a df from gene list, genes as rows
        gene_output_df = pd.DataFrame(gene_list, columns=['Genes with less than 100% 30x coverage'])
        return gene_output_df
    
    #output to as a CSV
    def output_csv(self, gene_df):
        output_file = 'Output.csv'
        gene_df.to_csv(output_file, index=False)
        


manager_object=Manager()
        