<html>
<head>
	<title>Sorting Hat</title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
	<style>
		body{
			padding:0;
			margin: 0;
			background-color: #000;
		}
		.main{
			width: 800px;
			min-height: 800px;
			margin: 0 auto;
			background: url('hpBackground2.png') no-repeat;
			padding-left: 100px;
			padding-right: 100px;
			text-align: center;
		}
		.menu{
			width: 500px;
			float: right;
			display: inline-block;
		}
		.menu li{
			display: inline;
			list-style-type: none;
		    padding-top: 74px;
		    width: 100px;
    		float: right;

		}
		.menu a{
			color: white;
		}
		.twoSent{
			padding-bottom: 0px;
			padding-top: 45px;
			font-size:22px;
		}
		#results{
			display: block; <!--Block shows it, None hides this -->
			padding-bottom: 10px;
			padding-top: 5px;
			font-size:22px;
		}		
		#analyzeText{
			display: none; <!-- None hides this -->
			padding-bottom: 10px;
			padding-top: 5px;
			font-size:22px;		
		}
		.clear{
			clear: both;
		}
		.logo{
			width: 300px;
			height: 100px;
			display: inline-block;
			float: left;
		}
	</style>
	
	
</head>
<body>
	<div class="main">
		<a href="hogwarts.html"><div class="logo"></div></a>
		<div class="menu">
			<ol>
				<li><a href="hpAnalyze.php">Analyze</a></li>
				<li><a href="hpCode.html">Code</a></li>
				<li><a href="hpAboutUs.html">About Us</a></li>
				<li><a href="hogwarts.html">Home</a></li>	
			</ol>
		</div>
		<div class="clear">
		</div>
		<?php
						if(isset($_REQUEST['req']) && isset($_REQUEST['hogwarts'])){
							echo '<div style="padding-top: 70px; width:100%;text-align:center; font-size:22px;"><b>Results:</b></div><img src="hp'.urldecode($_REQUEST['req']).'.png"/>';
						}
					?>

		
	
					<?php
						if(isset($_REQUEST['req']) && !isset($_REQUEST['hogwarts'])){
							echo '<div style="padding-top: 70px;width:100%;text-align:center; font-size:22px;"><b>Results:</b></div><img src="hp'.urldecode($_REQUEST['req']).'.png"/>';
						}
					?>
					
		<div class="twoSent">
			Type in a twitter handle to analyze tweets.
		</div>
		<div class="tb">
			<form method="get" action="pythonscript.php">
			<input type="text" name="handleText" style="font-size:22px; width:250px; height: 40px"/>
			<input type="submit" value="Submit" style="font-size:20px; width:100px; height: 40px" />
		</form>
		</div>					
		<!-- Analyzing tweets text -->
		<div id ="analyzeText">
			<center> <b> Analyzing your tweets.... </b> </center>
			<center> <b>Give us a minute. </b> </center>
		</div>
	</div>

</body>
</html>