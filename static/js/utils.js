function addEvent( obj, type, fn ) {
  if (obj.addEventListener) {
    obj.addEventListener( type, fn, false );
    EventCache.add(obj, type, fn);
  }
  else if (obj.attachEvent) {
    obj["e"+type+fn] = fn;
    obj[type+fn] = function() { obj["e"+type+fn]( window.event ); }
    obj.attachEvent( "on"+type, obj[type+fn] );
    EventCache.add(obj, type, fn);
  }
  else {
    obj["on"+type] = obj["e"+type+fn];
  }
}

var EventCache = function(){
  var listEvents = [];
  return {
    listEvents : listEvents,
    add : function(node, sEventName, fHandler){
      listEvents.push(arguments);
    },
    flush : function(){
      var i, item;
      for(i = listEvents.length - 1; i >= 0; i = i - 1){
        item = listEvents[i];
        if(item[0].removeEventListener){
          item[0].removeEventListener(item[1], item[2], item[3]);
        };
        if(item[1].substring(0, 2) != "on"){
          item[1] = "on" + item[1];
        };
        if(item[0].detachEvent){
          item[0].detachEvent(item[1], item[2]);
        };
        item[0][item[1]] = null;
      };
    }
  };
}();

function element() {
  var elements = new Array();
    for (var i = 0; i < arguments.length; i++) {
      var element = arguments[i];
      if (typeof element == 'string')
        element = document.getElementById(element);
      if (arguments.length == 1)
        return element;
      elements.push(element);
    }
  return elements;
}

function toggle() {
  for (var i=0; i < arguments.length; i++ ) {
    element(arguments[i]).style.display = (element(arguments[i]).style.display != 'none' ? 'none' : '' );
  }
}

function toggleVisibility(id,val) {
 var o=document.getElementById(id);
 if (val==0)
  o.style.display = 'none';
 else
  o.style.display = 'inline';
}

function enableField(item,val) {
 item.disabled = !val;
 if ((val==0) && item.value)
  item.value = "";
}

function enableRadio(item,val,valDefault) {
 item.disabled = !val;
 if ((val==1) && item.type=="radio")
  item.value = valDefault;
}

function checkEmpty(item, name) {
 var msg="";
 if (!item.value || item.value == '') msg += "The " + name + " cannot be empty.\n";
 return msg;
}

function checkNumber(item,name) {
 var msg="";
 var number = item.value;
 if(!item.value || isNaN(item.value || item.value == '')){
   msg = "The " + name + " value is not a number or empty.\n";
 }else if(Math.sign(number) === -1){
    msg = "The " + name + " value is not a positive number.\n";
 }
 //else{
      //msg = "The " + name + " value is not a number.\n";}
 return msg;
}

function checkNumberMinMax(item,name,mini,maxi) {
 var msg="";
 if (!item.value || isNaN(item.value))
   msg = "The " + name + " value is not a number.\n";
 else if (item.value < mini || item.value > maxi)
   msg = "The " + name + " value must be between " + mini + " and " + maxi + ".\n";
 return msg;
}

function checkTextFile(value, name) {
 var msg = "";
 if (value=="")
   msg += "The " + name + " name cannot be empty.\n";
 else {
   var extension = "";
   var extensionidx = value.search(/\.[A-Za-z]+$/);
   if (extensionidx!=-1) {
     extension = value.substr(extensionidx+1);
     if (extension!="txt" && extension!="phy" && extension!="aln" && extension!="fa" && extension!="fasta" && extension!="tre" && extension!="tree" && extension!="nwk") {
       if (!confirm("The " + name + " name has the \"" + extension + "\" extension \nand this program will only process files in text format.\n Is your file a text file ?"))
       msg += "The " + name + " file has to be a text file.\n";
     }
   }
 }
 return msg;
}

function checkPhylipFile(value, name) {
 var msg = "";
 if (value=="")
   msg += "The " + name + " name cannot be empty.\n";
 else {
   var extension = "";
   var extensionidx = value.search(/\.[A-Za-z]+$/);
   if (extensionidx!=-1) {
     extension = value.substr(extensionidx+1);
     if (extension!="phy") {
       if (!confirm("The " + name + " name has the \"" + extension + "\" extension \nand this program will only process files in PHYLIP format.\n Is your file in PHYLIP format ?"))
          msg += "The " + name + " file has to be in PHYLIP format.\n";
      }
    }
  }
    return msg;
  };

function checkTextAreaPhylip(value,name){
    var msg = "";
    if (value == "")
      msg += "The " + name + " name cannot be empty.\n";
    else {
      //var seq = "";
      var seq = value.trim();// split on newlines...
      seq = seq.replace(/[\r]/g,'')
      var epline = seq.split('\n');// check for header
      //console.log(epline)
      var d = parseInt(epline[0])
      var array = epline[0].split(" ").map(Number);
      if (Number.isInteger(array[0])  && Number.isInteger(array[1]) ) {
            var f = epline.splice(0,1);
            var lines= f.splice(0,1);
            if (epline[0] == undefined)
                msg += "Please enter amino acid sequence in second line";
                if (epline.length != array[0] && epline.length != array[0]*2)
              	     //console.log("fomat correcte")
                     msg += "format incorrecte";
               //else{msg += "The " + name + " has an incorrect format.\n";}
      }else{
            msg+="First line should start with integer and amino-acid or DNA sequence in next line";
            }
        }
      return msg;
    };
