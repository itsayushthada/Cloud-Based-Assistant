#! /usr/bin/python36

print("content-type: text/html")
print("\n")

print("""
<!DOCTYPE html>
<html>
	<head>
		<script>
		
		    // Put event listeners into place
		    window.addEventListener("DOMContentLoaded", function() 
		    {
			    var canvas = document.getElementById('canvas');
			    var context = canvas.getContext('2d');
			    var video = document.getElementById('video');
			    var mediaConfig =  { video: true };
			    
			    var errBack = function(e) 
			    {
			    	console.log('An error has occurred!', e)
			    };

			    // Put video listeners into place
			    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) 
			    {
				navigator.mediaDevices.getUserMedia(mediaConfig).then(function(stream) {
				    video.src = window.URL.createObjectURL(stream);
				    video.play();
				});
			    }

			    /* Legacy code below! */
			    else if(navigator.getUserMedia) 
			    { // Standard
						navigator.getUserMedia(mediaConfig, function(stream) {
							video.src = stream;
							video.play();
						}, errBack);
			    } 
			    else if(navigator.webkitGetUserMedia) 
			    { // WebKit-prefixed
						navigator.webkitGetUserMedia(mediaConfig, function(stream){
							video.src = window.webkitURL.createObjectURL(stream);
							video.play();
						}, errBack);
			    } 
			    else if(navigator.mozGetUserMedia) 
			    { // Mozilla-prefixed
						navigator.mozGetUserMedia(mediaConfig, function(stream){
							video.src = window.URL.createObjectURL(stream);
							video.play();
						}, errBack);
			    }

			    // Trigger photo take
			    document.getElementById('snap').addEventListener('click', function() 
			    {
				context.drawImage(video, 0, 0, 640, 480);
			    });
		    }, false);	
		    
		    function convertCanvasToImage() 
		    {
		    	var canvas = document.getElementById("canvas");
			var data = canvas.toDataURL("image/png");
			sessionStorage.setItem("key", data);
			document.forms["faceToServer"].submit();		
		    }
		</script>
	</head>
	
	<body>
		<form name="faceToServer" action="serverpage.py" method="post">
		</form>
		
		<table border=1>
			<tr>
				<td> 
					<video id="video" width="640" height="480" autoplay></video>
					<canvas id="canvas" width="640" height="480"></canvas>
				</td>
			</tr>	
					
			<tr>		
				<td>
					<button id="snap">Snap Photo</button>
				</td>
				<td>
					<button id="save" onclick="convertCanvasToImage()">Save Photo</button>
				</td>
			</tr>
		</table>
	</body>
</html>
""")
