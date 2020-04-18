			//create a constructor function to be used in the end

			function Suggest()
			{
				othis=this;//save this for future
				this.xhr=new XMLHttpRequest();
				this.SRNpart=null;

				this.div=null;

				//create a timer(to decide when to go to server)
				this.timer=null;

				this.getSRN=function()
				{
					if(this.timer)
					{
						clearTimeout(this.timer);
					}
					//get ready to go to server in 1 second
					//if the user types something before 1 second, this function will be called and the timer is cancelled before registering a new one
					//if the user keeps quite for more than 1 second the fetchMovie function is called anyways

					this.timer=setTimeout(this.fetchSRN,1000);
				}
				//function to check if we need to go
				this.fetchSRN=function()
				{
					//Check if movie textbox is blank. This can happen if the user repeatedly used the backspace to clear the box
					othis.SRNpart=document.getElementById("srn");
					if(othis.SRNpart.value=="")
					{
						othis.div=document.getElementById("container");
						othis.div.innerHTML="";
						othis.div.style.display=none;

					}
					else
					{
						//BUild the key to search in localStorage
						key="http://127.0.0.1:5000/static/php/suggest.php?SRNpart="+othis.SRNpart.value;
						if(localStorage[key])//We need to check in cache
						{
							//alert(localStorage[key]);
							//if we have it in the cache, show the movie list corresponding to this movie;;;how to check, go to networks and make sure GET isnt there
							//alert(localStorage[key]);
							othis.div=document.getElementById("container");
							othis.div.innerHTML="";
							SRNlist=JSON.parse(localStorage[key]);
							for(i=0;i<SRNlist.length;i++)
							{
								newdiv=document.createElement("div");
								newdiv.innerHTML=SRNlist[i];
								//newdiv.className="suggest";
								othis.div.appendChild(newdiv);

								//now register for the click
								newdiv.onclick=othis.setSRN;
							}
							//show the container
							othis.div.style.display="block";
						}
						else//no choice but to go to the server
						{
							othis.xhr.onreadystatechange=othis.processRes;//window will call this function on xhr otherwise control is with window only
							othis.xhr.open("GET","http://127.0.0.1:5000/static/php/suggest.php?SRNpart="+othis.SRNpart.value,true);
							othis.xhr.send();
						}
					}
				}//end of fetch movies
				this.processRes=function()
				{
					//alert("suo")
					if(this.readyState==4 && this.status==200)
					{
						//First parse the json sent by the server
						//cleanup the div before populating new movies
						//alert(this.responseURL);
						SRNs=JSON.parse(this.responseText);
						othis.div=document.getElementById("container");
						othis.div.innerHTML="";
						//alert(this.responseText);
						if(SRNs.length==0)
						{
							//Server could not find any suggestions
							
							othis.div.style.display="none";
						}
						else//We have some suggestions
						{
							//alert(movies)
							for(i=0;i<SRNs.length;i++)
							{
								newdiv=document.createElement("div");
								newdiv.innerHTML=SRNs[i];
								//newdiv.className="suggest";
								othis.div.appendChild(newdiv);

								//now register for the click
								newdiv.onclick=othis.setSRN;
							}
							//show the container
							othis.div.style.display="block";

							//save to localStorage for later use
							localStorage[this.responseURL]=this.responseText;
						}
					}
				}
				//when user selects a movie from the list, set into the textbox and clear the container div
				this.setSRN=function()
				{
					othis.SRNpart.value=this.innerHTML;
					othis.div.innerHTML="";
					othis.div.style.display="none";
				}

			}
			obj=new Suggest();

			