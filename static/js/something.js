function getlist(){
    var getData = $.get('/SRNsearch?SRN='+document.getElementById("srn").value);
    getData.done(function(results)
    {
        var SRNvalues = results.data;
        //console.log(SRNvalues);
        //console.log(SRNvalues.length);
        this.SRNpart=document.getElementById("srn");
        if(this.SRNpart.value=="")
		{
			this.div=document.getElementById("container");
			this.div.innerHTML="";
			this.div.style.display=none;

		}
        this.div=document.getElementById("container");
        this.div.innerHTML="";
        if(SRNvalues.length==0)
        {
            //Server could not find any suggestions
            this.div.style.display="none";
        }
        for(i=0;i<SRNvalues.length;i++)
        {
            newdiv=document.createElement("div");
            newdiv.innerHTML=SRNvalues[i];
            //newdiv.className="suggest";
            this.div.appendChild(newdiv);
            //now register for the click
            //newdiv.onclick=this.setSRN;
            newdiv.onclick=function(){
                //console.log("enter");
                document.getElementById("srn").value=this.innerHTML;
                //console.log("exit");
                document.getElementById("container").innerHTML="";
                //this.div.style.display="none";
            }

        }
        this.div.style.display="block";
    });
}

    

