import os
import streamlit as st

from Bio import AlignIO

from ..runPhyML import RunPhyML

# Page settings
st.set_page_config(
    page_title = "PhyML - New analysis",
    layout = "wide",
)

# Basic options
with st.container(border = True):

    inputCol1, inputCol2 = st.columns(2)
    sequences = None
    with inputCol1:
        st.write("Sequences input type (phylip format):")
        input = st.radio(
            "Sequences input type (phylip format)",
            ["File", "Input box"],
            key = ["file", "box"],
            label_visibility  = "collapsed",
            horizontal = True
        )
    with inputCol2:
        if input == "File":
            file = st.file_uploader(
                "Select file:",
                type = ['phy']
            )
            if file != None:
                sequences = AlignIO.read(file)
        elif input == "Input box":
            sequences = st.text_area("Sequences:")
    
    st.write("Data type:")
    dataTypeMap = {
        "nt": "Nucleotides",
        "aa": "Amino-Acids"
    }
    dataType = st.radio(
        "Data type",
        dataTypeMap.keys(),
        format_func = lambda option: dataTypeMap[option],
        label_visibility  = "collapsed",
        horizontal = True
    )

    st.write("Sequences organization:")
    seqOrg = st.radio(
        "Sequences organization",
        ["Interleaved","Sequential"],
        label_visibility  = "collapsed",
        horizontal = True
    )

    multiCol1, multiCol2 = st.columns(2)
    with multiCol1:
        st.write("Number of datasets in the input:")
    with multiCol2:
        nbDS = st.number_input(
            "Number of datasets",
            min_value = 1,
            max_value = 100,
            label_visibility  = "collapsed",
        )

# Advanced options
with st.expander("Advanced options"):
    st.write("Use minimum parsimony tree (BioNJ)?")
    parsTree = st.radio(
        "Use minimum parsimony tree (BioNJ)?",
        ["Yes","No"],
        index = 1,
        label_visibility  = "collapsed",
        horizontal = True
    )
    
    valCol1, valCol2 = st.columns(2)
    with valCol1:
        st.write("Validation method:")
        valMethod = st.radio(
            "Validation method",
            ["No validation", "Bootstrap", "Approximate likelihood"],
            index = 2,
            label_visibility  = "collapsed",
            horizontal = True
        )
    with valCol2:
        if valMethod == "No validation":
            bootstrap = 0
        elif valMethod == "Bootstrap":
            bootstrap = st.number_input(
                "Bootstrap iterations",
                min_value = 1,
                max_value = 1000,
                label_visibility  = "hidden",
            )
        elif valMethod == "Approximate likelihood":
            valMap = {
                -1: "aLRT",
                -2: "Chi2",
                -4: "SH",
                -5: "Bayes",
            }
            bootstrap = st.segmented_control(
                "Approximate likelihood",
                options = valMap.keys(),
                format_func = lambda option: valMap[option],
                default = -4,
                selection_mode = "single",
                label_visibility  = "hidden",
            )

    modelCol1, modelCol2 = st.columns(2)
    with modelCol1:
        st.write("Substitution model:")
    with modelCol2:
        if dataType == "nt":
            model = st.segmented_control(
                "Subtitution model",
                options = ["HKY85", "JC69", "K80", "F81", "F84", "TN93", "GTR"],
                default = "HKY85",
                selection_mode = "single",
                label_visibility  = "collapsed",
            )
        elif dataType == "aa":
            model = st.segmented_control(
                "Subtitution model",
                options = ["LG", "WAG", "JTT", "MtREV", "Dayhoff", "DCMut", "RtREV", "CpREV", "VT", "Blosum62", "MtMam", "MtArt", "HIVw",  "HIVb"],
                default = "LG",
                selection_mode = "single",
                label_visibility  = "collapsed",
            )
    
    eqCol1, eqCol2 = st.columns(2)
    with eqCol1:
        st.write("Equilibrium frequencies:")
    with eqCol2:
        equilibriumMap = {
            "e": "Empirical",
            "m": "Model",
            "freq": "Frequencies",
        }
        if dataType == "nt":
            equilibrium = st.segmented_control(
                "Equilibrium frequencies",
                options = equilibriumMap.keys(),
                default = "e",
                format_func = lambda option: equilibriumMap[option],
                selection_mode = "single",
                label_visibility  = "collapsed",
            )
        elif dataType == "aa":
            equilibrium = st.segmented_control(
                "Equilibrium frequencies",
                options = list(equilibriumMap.keys())[0:2],
                default = "e",
                format_func = lambda option: equilibriumMap[option],
                selection_mode = "single",
                label_visibility  = "collapsed",
            )
        if equilibrium == "freq":
            eqSubCol1, eqSubCol2, eqSubCol3, eqSubCol4 = st.columns(4)
            with eqSubCol1:
                fA = st.number_input(
                    "A nucleotides",
                    min_value = 0.0,
                    max_value = 1.0,
                    value = 0.25,
                )
            with eqSubCol2:
                fC = st.number_input(
                    "C nucleotides",
                    min_value = 0.0,
                    max_value = 1.0,
                    value = 0.25,
                )
            with eqSubCol3:
                fG = st.number_input(
                    "G nucleotides",
                    min_value = 0.0,
                    max_value = 1.0,
                    value = 0.25,
                )
            with eqSubCol4:
                fT = st.number_input(
                    "T nucleotides",
                    min_value = 0.0,
                    max_value = 1.0,
                    value = 0.25,
                )
            freqSum = fA + fC + fG + fT
            if freqSum != 1.0:
                st.error(f"Error! The sum of frequencies for all nucleotides must be 1.0 but it is {freqSum}!")
            
            equilibrium = ",".join([str(fA),str(fC),str(fG),str(fT)])

    ts_tvCol1, ts_tvCol2 = st.columns(2)
    with ts_tvCol1:
        st.write("Transition / transversion ratio:")
        ts_tvType = st.radio(
            "Transition / transversion ratio",
            ["Estimated", "Fixed"],
            label_visibility  = "collapsed",
            horizontal = True
        )
    with ts_tvCol2:
        if ts_tvType == "Fixed":
            ts_tvRatio = st.number_input(
                "Transition / transversion ratio",
                min_value = 1.0,
                format="%0.1f",
                label_visibility  = "hidden",
            )
        else:
            ts_tvRatio = "e"
    
    proportionCol1, proportionCol2 = st.columns(2)
    with proportionCol1:
        st.write("Proportion of invariable sites:")
        proportionType = st.radio(
            "Proportion of invariable sites",
            ["Estimated", "Fixed"],
            label_visibility  = "collapsed",
            horizontal = True
        )
    with proportionCol2:
        if proportionType == "Fixed":
            proportion = st.slider(
                "Transition / transversion ratio",
                min_value = 0.0,
                max_value = 1.0,
                value = 0.5,
                label_visibility  = "hidden",
            )
        else:
            proportion = "e"

    subCol1, subCol2 = st.columns(2)
    with subCol1:
        st.write("Number of substitution rate categories:")
    with subCol2:
        nbSubstitutions = st.number_input(
            "Number of substitution rate categories",
            min_value = 0.0,
            value = 4.0,
            format="%0.1f",
            label_visibility  = "collapsed",
        )

    gammaCol1, gammaCol2 = st.columns(2)
    with gammaCol1:
        st.write("Gamma shape parameter:")
        gammaType = st.radio(
            "Gamma shape parameter",
            ["Estimated", "Fixed"],
            label_visibility  = "collapsed",
            horizontal = True
        )
    with gammaCol2:
        if gammaType == "Fixed":
            gamma = st.number_input(
                "Gamma shape parameter",
                min_value = 1.0,
                format="%0.1f",
                label_visibility  = "hidden",
            )
        else:
            gamma = "e"

    treeCol1, treeCol2 = st.columns(2)
    with treeCol1:
        st.write("Tree topology improvement:")
    with treeCol2:
        tree = st.segmented_control(
            "Tree topology improvement",
            options = ["NNI", "SPR", "BEST"],
            default = "NNI",
            selection_mode = "single",
            label_visibility  = "collapsed",
        )

    optCol1, optCol2 = st.columns(2)
    with optCol1:
        st.write("Tree parameters optimisation:")
        paramsOptType = st.radio(
            "Tree parameters optimisation",
            ["None", "Optimize parameters"],
            label_visibility  = "collapsed",
            horizontal = True
        )
    with optCol2:
        if paramsOptType == "Optimize parameters":
            paramsOptMap = {
                "t": "Tree topology",
                "l": "Branch length",
                "r": "Rate"
            }
            paramsOptimisation = st.segmented_control(
                "Tree parameters for optimisation",
                options = paramsOptMap.keys(),
                format_func = lambda option: paramsOptMap[option],
                selection_mode = "multi",
                label_visibility  = "hidden",
            )
        else:
            paramsOptimisation = "n"
    
    randStart = None
    nbInitialTrees = 0
    if tree == "SPR":
        st.write("Should the initial tree be random?")
        randStart = st.radio(
            "Should the initial tree be random?",
            ["Yes","No"],
            index = 1,
            label_visibility  = "collapsed",
            horizontal = True
        )

        SPRRandCol1, SPRRandCol2 = st.columns(2)
        with SPRRandCol1:
            st.write("Number of initial random trees:")
        with SPRRandCol2:
            nbInitialTrees = st.slider(
                "Number of initial random trees",
                min_value = 10,
                max_value = 100,
                label_visibility  = "collapsed",
            )

# Submit form on click
if st.button("Launch analysis"):
    userInputMap = {
        "input": sequences,
        "datatype": dataType,
        "sequential": True if seqOrg == "Sequential" else False,
        "multiple": nbDS,
        "pars": True if "Yes" else False,
        "bootstrap": bootstrap,
        "model": model,
        "equilibrium": equilibrium,
        "ts/tv": ts_tvRatio,
        "pinv": proportion,
        "nclasses": nbSubstitutions,
        "alpha": gamma,
        "search": tree,
        "params": paramsOptimisation
    }

    if tree == "SPR":
        userInputMap["rand_start"] = randStart
        userInputMap["n_rand_starts"] = nbInitialTrees
    
    