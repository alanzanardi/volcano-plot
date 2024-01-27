# volcano-plot :volcano: 
These scripts were used for generating a Volcano plot, a data visualization technique commonly used in proteomics and other fields to identify significant changes in expression levels between two conditions.<br>
<br>
Hoping they can be useful to you as example from which collecting inspiration for your specific cases.<br>
<br>
**\*\*\* DISCLAIMER \*\*\*** these scripts were written to help me in my laboratory data analysis work. The example I used to explain how they work show totally random values, in any case each data contained here should be trated as confidential. Thank you for the support.<br>
<br>
## Content :open_book:<br>
**:small_red_triangle_down:volcano_plot.py:** this script is for generating Volcano plot images for publication purposes (Fig. 1). Data, both statistically and biologically significant, are shown in blue. <br><br>
**Figure 1**<br>
<img src="https://github.com/alanzanardi/volcano-plot/blob/main/Fig1.jpg">
<br>
**:small_red_triangle_down:interatcive_volcano_plot.py:** this script is used to generate an interactive Volcano plot via HTML (Fig. 2). The purpose is to provide a tool for quickly identifying the gene of interest on the graph.<br>
<br>
**Figure 2**<br>
<br>
**:small_red_triangle_down:Benjamini_Hochberg_correction.py:** this optional script is used to perform the False Discovery Rate (FDR) correction, using the Benjamini-Hochberg (BH) correction.
<br>
<br>
**:small_red_triangle_down:test_volcano_plot.csv** this example dataset was used to test volcano_plot.py and interactive_volcano_plot.py, and generate Fig.1 and Fig.2<br>
<br>
**:small_red_triangle_down:test_BH_correction.csv** this is an example dataset that you can use as a test for Benjamini_Hochberg_correction.py<br>
