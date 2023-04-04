import streamlit as st
import streamlit.components.v1 as com
with open("styles.css") as source:
    styles=source.read()    
com.html("""

  <nav>
    <div class="nav-wrapper">
      <a href="#" class="brand-logo">Logo</a>
      <ul id="nav-mobile" class="right hide-on-med-and-down">
        <li><a href="Home.py">Home</a></li>
        <li><a href="AutoMlRegressionApp.py">AutoMlRegressionApp</a></li>
        <li><a href="AutoMlClassificationApp.py">AutoMlClassificationApp</a></li>
        <li><a href="TheMachineLearningHyperparameterOptimizationApp.py">TheMachineLearningHyperparameterOptimizationApp</a></li>
        <li><a href="options.py">options</a></li>
        <li><a href="configuration.py">configuration</a></li>
      </ul>
    </div>
  </nav>


""")







