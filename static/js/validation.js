function model(){
  var o = document.options;
  //Model field
  enableField(o.model,o);
  //Frequencies
  enableRadio(o.FqOption[0], o, "n")
  enableRadio(o.FqOption[1], o, "m");
  enableRadio(o.FqOption[2], o, "e");
  enableRadio(o.FqOption[3], o, "0.25, 0.25, 0.25, 0.25");
  //Transition/Transversion
   enableRadio(o.tstv[0], o.SequenceTypeOption[0].checked, "");
   enableRadio(o.tstv[1], o.SequenceTypeOption[0].checked, "e");
   enableField(o.Kappa,o.SequenceTypeOption[0].checked && o.tstv[0].checked);
  //Invar option
  enableRadio(o.pinv[0],o, "");
  enableRadio(o.pinv[1],o, "e");
  enableField(o.Invar,o && o.pinv[0].checked);
  //Gamma option
  enableRadio(o.alpha[0],o, "");
  enableRadio(o.alpha[1],o, "e");
  //enableField(o.nclasses,o);

  enableField(o.Gamma, o.alpha[0].checked);
  enableRadio(o.nclassesOption[0],o, "");
  enableRadio(o.nclassesOption[1],o, "e");
  o.nclasses.value=4; nclassesChanged();

  fillModelMenu();
}

function modelChanged() {
 var K, Koption;
 var o = document.options;
 //
 if (o) { //changement0.model
  switch(o.model.value) {
   //
   case "JC69": case "F81": case "GTR":
    K=0; Koption=0;
    o.tstv[0].checked = true;
   break;
   //
   case "TN93":
    K=0; Koption=0;
    o.tstv[1].checked = true;
   break;
   //
   case "K80": case "F84": case "HKY85":
    K=0; Koption=1;
    o.tstv[1].checked = true;
   break;
   //
   default:
    K=0; Koption=0;
    o.tstv[1].checked = true;
   break;
  }
  enableField(o.Kappa,K);
  enableRadio(o.tstv[0],Koption,"");
  enableRadio(o.tstv[1],Koption,"e");
 }
}

function fillModelMenu() {
 var o = document.options;
 if (o) {
  var menuOptions, sel, i;
  // DNA
  if (o.SequenceTypeOption[0].checked) {
   menuOptions = new Array(7);
   menuOptions[0]="JC69";
   menuOptions[1]="K80";
   menuOptions[2]="F81";
   menuOptions[3]="F84";
   menuOptions[4]="HKY85"; sel = 4;
   menuOptions[5]="TN93";
   menuOptions[6]="GTR";
  }
  // Protein
  else {
   menuOptions = new Array(15);
   menuOptions[0]="Blosum62";
   menuOptions[1]="CpREV";
   menuOptions[2]="Dayhoff";
   menuOptions[3]="DCMut";
   menuOptions[4]="FLU";
   menuOptions[5]="HIVb";
   menuOptions[6]="HIVw";
   menuOptions[7]="JTT";
   menuOptions[8]="LG"; sel = 8;
   menuOptions[9]="MtArt";
   menuOptions[10]="MtMam";
   menuOptions[11]="MtREV";
   menuOptions[12]="RtREV";
   menuOptions[13]="VT";
   menuOptions[14]="WAG";
  }
  o.model.length = menuOptions.length;
  for(i=0; i<menuOptions.length; i++)
   o.model[i] = new Option(menuOptions[i], menuOptions[i]);
   //
  o.model.selectedIndex = sel;
 }
 //
 modelChanged();
}

function aff() {

    document.getElementById("Fq_center").style.visibility = "visible";

}

function cac() {

    document.getElementById("Fq_center").style.visibility = "hidden";

}

function aff1() {

    document.getElementById("Fq_").style.visibility = "visible";

}

function cac1() {

    document.getElementById("Fq_").style.visibility = "hidden";

}

function sequenceTypeChanged() {
 var o = document.options;
 if (o){
  //
  fillModelMenu();
  //
  var FqOptionLabelno = document.getElementById("Fq_no");
  var FqOptionLabelLeft = document.getElementById("Fq_left");
  var FqOptionLabelRight = document.getElementById("Fq_right");
  var FqOptionLabelCenter = document.getElementById("Fq_center");
  var FqOptionLabel = document.getElementById("Fq_");
  // DNA
  if (o.SequenceTypeOption[0].checked) {
       aff();
       aff1();
   //
   FqOptionLabelno.innerHTML="no";
   FqOptionLabelLeft.innerHTML="optimized";
   FqOptionLabelCenter.innerHTML="Frequencies"
   FqOptionLabelRight.innerHTML="empirical";
   o.FqOption[0].checked = true;
  //
  }
  // Protein
  else if (o.SequenceTypeOption[1].checked){
      cac();
      cac1();
   //
   FqOptionLabelno.innerHTML="no";
   FqOptionLabelRight.innerHTML="empirical";
   FqOptionLabelLeft.innerHTML="model";
   FqOptionLabelCenter.innerHTML="Frequencies"
   o.FqOption[0].checked = true;
   //
  }
 }
}

function fillMovementMenu(menu) {
  var sel;
  if (menu.type!="select-one") return;
  menu.length = 4;
  menu[0]= new Option("No search", "n");sel = 0
  menu[1]= new Option ("NNI", "NNI");
  menu[2]= new Option ("SPR","SPR");
  menu[3]= new Option ("BEST", "BEST");
  menu.selectedIndex = 0;
}

function optimizeMenu(menu){
  var sel;
  if (menu.type!="select-one") return;
  menu.length = 6;
  menu[0] = new Option("Aucune optimisation", "n");sel=0;
  menu[1] = new Option("Optimisation tlr", "tlr");
  menu[2] = new Option("Optimisation tl", "tl");
  menu[3] = new Option("Optimisation lr", "lr");
  menu[4] = new Option("Optimisation l", "l");
  menu[5] = new Option("Optimisation r", "r");
  menu.selectedIndex = 0;
  }

function searchChanged() {
  var o = document.options;
 //
 if (o.search.value!="BEST" & o.search.value!="SPR")
   o.randstart[1].checked=1;
 //
 randomOptionChanged();
}

function optimisationTotale(){
  var o = document.options;
  enableField(o.search, true)
  if (o.params.value!="tlr" & o.params.value!="tl"){
    enableField(o.search, false);
  }
  //
  else {
    searchChanged();
  }
}

function fillRandomMenu(menu) {
  var i;
  var menuOptions = new Array(10);
  if (menu.type!="select-one") return;
  menuOptions[0]="1";
  menuOptions[1]="2";
  menuOptions[2]="3";
  menuOptions[3]="4";
  menuOptions[4]="5";
  menuOptions[5]="6";
  menuOptions[6]="7";
  menuOptions[7]="8";
  menuOptions[8]="9";
  menuOptions[9]="10";
  menu.length = menuOptions.length;
  for(i=0; i<menuOptions.length; i++)
    menu[i] = new Option(menuOptions[i], menuOptions[i]);
  menu.selectedIndex = 4;
}

function fillPositionMenu(menu) {
  var i;
  var menuOptions = new Array(3);
  if (menu.type!="select-one") return;
  menuOptions[0]="1";
  menuOptions[1]="2";
  menuOptions[2]="3";
  menu.length = menuOptions.length;
  for(i=0; i<menuOptions.length; i++)
    menu[i] = new Option(menuOptions[i], menuOptions[i]);
  menu.selectedIndex = 0;
}

function randomOptionChanged() {
 var o = document.options;
 //
 if ((o.search.disabled) || (o.search.value!="BEST" && o.search.value!="SPR"))
   enableRadio(o.randstart[0], false, "");
 else
   enableRadio(o.randstart[0], true, "rand_start");
 //
 enableField(o.nRandStarts, o.randstart[0].checked);
}

function codposOptionChanged() {
 var o = document.options;
 //
 if (o.codposOption[0].checked) {
   o.codpos.checked=1;
 }
 //
 enableField(o.codpos, o.codposOption[0].checked);
}

function fillTestMenu(menu) {
  if (menu.type!="select-one") return;
  menu.length = 5;
  menu[0] = new Option("aLRT SH-like", "-4");
  menu[1] = new Option("aLRT Chi2-based", "-2");
  menu[2] = new Option("minimum Chi2-based & SH-like", "-3");
  menu[3] = new Option("aLRT Statistics", "-1");
  menu[4] = new Option("aBayes", "-5");
  menu.selectedIndex = 0;
}

function aLRTOptionChanged() {
 var o = document.options;
 //
 if (o.OptaLRTOption[0].checked)
   o.bootstrapOption[1].checked=1;
 bootOptionChanged();
 //
 enableField(o.TestValue, o.OptaLRTOption[0].checked);
}

function dataSetChange(){
  var o = document.options;
  if (o.multiple[0].checked) {
    o.NbDataSets.value=1;
  }
  //
  enableField(o.NbDataSets, o.multiple[0].checked);
}

function runIdChange(){
  var o = document.options;
  if (o.runId[0].checked) {
    o.idString.checked=1;
  }
  //
  enableField(o.idString, o.runId[0].checked);
}

function quietModeChanged(){
  var o = document.options;
  if (o.quietMode[0].checked) {
    o.quietMode.checked=1;
  //
  enableRadio(o.quietMode[0],(!o.quietMode[1].checked), "quiet")
  }
}

function ancestralCalculateChanged(){
  var o = document.options;
  if (o.ancestralCalculate[0].checked) {
    o.ancestralCalculate.checked=1;
  //
  enableRadio(o.ancestralCalculate[0],(!o.ancestralCalculate[1].checked), "ancestral")
  }
}

function leaveDuplicatesChanged(){
  var o = document.options;
  if (o.leaveDuplicates[0].checked) {
    o.leaveDuplicates.checked=1;

  //
  enableRadio(o.leaveDuplicates[0],(!o.leaveDuplicates[1].checked), "leave_duplicates")
  }
}

function bootOptionChanged() {
 var o = document.options;
 //
 if (o.bootstrapOption[0].checked) {
   o.OptaLRTOption[1].checked=1;
   o.NbBtsDataSets.value=100;
 }
 //
 enableField(o.NbBtsDataSets, o.bootstrapOption[0].checked);
 enableField(o.TestValue, o.OptaLRTOption[0].checked);
}

function startingTreeChanged() {
 var o = document.options;
 //
 if (o.pars[0].checked) {
   o.pars.checked=1;
   //
 enableRadio(o.pars[0],(!o.pars[1].checked), "pars");
  }
}

function tstvChanged() {
 var o = document.options;
 //
 enableField(o.Kappa, o.tstv[0].disabled==0 && o.tstv[0].checked);
 //
 if (o.tstv[0].checked) {
  switch (o.model.value) {
   //
   case "JC69": case "F81": case "TN93": case "GTR":
    o.Kappa.value = 1;
   break;
   //
   case "K80": case "F84": case "HKY85":
    o.Kappa.value = 4;
   break;
   //
   default:
    o.Kappa.value = "";
   break;
  }
 }
}

function nclassesChanged() {
 var o = document.options;
 var b = (o.nclasses.value > 1);
 //
 //
 enableField(o.nclasses, o.nclassesOption[0].disabled==0 && o.nclassesOption[0].checked);
 //enableRadio(o.alpha[0], b, "");
 //enableRadio(o.alpha[1], b, "e");
 //enableField(o.Gamma, b && o.alpha[0].checked);
}

function alphaChanged() {
 var o = document.options;
 //
 enableField(o.Gamma, o.alpha[0].disabled==0 && o.alpha[0].checked);
}

function rSeedChanged() {
 var o = document.options;
 //
 enableField(o.rSeed, o.rSeedOption[0].disabled==0 && o.rSeedOption[0].checked);
}

function pinvChanged() {
 var o = document.options;
 //
 var tmp = o.Invar.value;// en l'activant il va afficher la valeur 0.0
 enableField(o.Invar, o.pinv[0].disabled==0 && o.pinv[0].checked);
 o.Invar.value=tmp; //en l'activant il va afficher la valeur 0.0
}

function noColaliasOptionChanged(){
  var o = document.options;
  if (o.noColalias[0].checked) {
      o.noColalias.checked=1;
    enableRadio(o.noColalias[0],(!o.noColalias[1].checked), "no_colalias");
  }
}

function printTraceOptionChanged(){
    var o = document.options;
  //
  if (o.printTrace[0].checked) {
    o.printTrace.checked=1;
  //
  enableRadio(o.printTrace[0],(!o.printTrace[1].checked), "print_trace");
  }
}

function jsonTraceOptionChanged(){
    var o = document.options;
  //
  if (o.jsonTrace[0].checked) {
    o.jsonTrace.checked=1;
  //
  enableRadio(o.jsonTrace[0],(!o.jsonTrace[1].checked), "json_trace");
  }
}

function noMemoryCheckOptionChanged(){
  var o = document.options;
  if (o.noMemoryCheck[0].checked) {
    o.noMemoryCheck.checked=1;
    enableRadio(o.noMemoryCheck[0],(!o.noMemoryCheck[1].checked), "no_memory_check");
  }
}

function printSiteLnlOptionChanged(){
    var o = document.options;
  //
  if (o.printSiteLnl[0].checked) {
    o.printSiteLnl.checked=1;
  //
  enableRadio(o.printSiteLnl[0],(!o.printSiteLnl[1].checked), "print_site_lnl");
  }
}

function useMedianChanged(){
    var o = document.options;
  //
  if (o.useMedian[0].checked) {
    o.useMedian.checked=1;
  //
  enableRadio(o.useMedian[0],(!o.useMedian[1].checked), "use_median");
  }
}

function inputFileChanged() {
 var o = document.options;

 if (o) {
  //
    enableField(o.file, o.DataOption[0].checked );
    if (o.DataOption[0].checked) {
      o.input.checked=1;
    }
    //
    enableField(o.input, o.DataOption[1].checked);

  //
    enableRadio(o.sequential[0], o, " ");
    enableRadio(o.sequential[1], o, " -q");
  //
    // re-initialize the form with default settings if no value and no userfile selected
    // enableRadio(o.SequenceTypeOption[0], b, "nt");
    // enableRadio(o.SequenceTypeOption[1], b, "aa");
     //o.sequential[0].checked=1;

     dataSetChange();
     codposOptionChanged();
     rSeedChanged();
    //
    // model set in sequenceTypeChanged
      o.tstv[1].checked=1; // Kappa set in modelChanged called by sequenceTypeChanged
      o.pinv[1].checked=1; pinvChanged();
    //
      o.nclasses.value=4; nclassesChanged();
    // alpha set in nclassesChanged
    //
      o.runId[1].checked=1; runIdChange();
      codposOptionChanged();
      //o.quietMode[1].checked=1;
      //o.ancestralCalculate[1].checked=1;
    //  o.leaveDuplicates[1].checked=1;
    startingTreeChanged();
    searchChanged();
    randomOptionChanged();

    //optimiseTopoOptionChanged();
    //optimiseBranchesOptionChanged();
    //
    bootOptionChanged();
    aLRTOptionChanged();
    }
  }

function validate() {
 var o = document.options;
 var msg="";
 //
 if (o.DataOption[0].checked)
    msg += checkPhylipFile(o.file.value, "input phylipfile");
  //
  if(o.DataOption[1].checked)
    msg += checkTextAreaPhylip(o.input.value, "textarea phylipfile");
  //
  //if (o.DataOption[1].checked)
    //msg += checkEmpty(o.input, "text phylipfile")
 //
 if (!o.NbDataSets.disabled){
      msg += checkNumberMinMax(o.NbDataSets, "number of data sets", 1, 100);
      msg += checkNumber(o.NbDataSets, "number of data sets")
    }
 //
 if (!o.NbBtsDataSets.disabled){
      msg += checkNumberMinMax(o.NbBtsDataSets, "number of bootstrapped data sets", 0, 1000);
      msg += checkNumber(o.NbBtsDataSets, "number of bootstrapped data sets");
    }
        // if (o.pars[0].checked)
        //   msg += checkTextFile(o.StartingTree.value, "starting tree file");
 if (o.SequenceTypeOption[0].checked && !o.Kappa.disabled){
      //msg += checkEmpty(o.kappa, "transition/transversion ratio")
      msg += checkNumber(o.Kappa, "transition/transversion ratio");
    }
 //
 // Check model paramters only when automatic model selection not choosen
  //
  if (!o.Invar.disabled){
      //  msg += checkEmpty(o.Invar, "proportion of invariable sites")
        msg += checkNumberMinMax(o.Invar, "proportion of invariable sites", 0.0, 1.0);
        msg += checkNumber(o.Invar, "proportion of invariable sites");
      }
  if (!o.nclasses.disabled){
      msg += checkNumber(o.nclasses, "number of substitution rates categories");
    }
  //
  if (!o.Gamma.disabled){
        msg += checkNumber(o.Gamma, "Gamma shape paramete");
      }
  //
  if (!o.rSeed.disabled){
        msg += checkNumber(o.rSeed, "Random number generator");
      }
  if (!o.idString.disabled){
        msg += checkEmpty(o.idString, "The ID string");
      }
 if (msg) {
      msg += "\n\nPlease make your corrections and re-submit the form.";
      alert (msg);
      return false;
    }
 else
  return true;
}

function DoLoad() {
  var o = document.options;
  //
  if (o) {
    //
    fillMovementMenu(o.search);
  //
    fillRandomMenu(o.nRandStarts);
  //
    fillTestMenu(o.TestValue);
  //
    optimizeMenu(o.params);
  //
    fillPositionMenu(o.codpos);
    //
    }
  //
  inputFileChanged();
  //
  dataSetChange();
  //  //
  sequenceTypeChanged();
  //
  model();
  //
  //tstvChanged();
  //
  //nclassesChanged();
  //
  //alphaChanged();
  //
  //pinvChanged();

  //usemedianChanged()
  //
  startingTreeChanged();
  //
  searchChanged();
  //
  randomOptionChanged();
  //
  //optimiseTopoOptionChanged();
  //
  //optimiseBranchesOptionChanged();
  //
  aLRTOptionChanged();
  //
  bootOptionChanged();
  //
}
