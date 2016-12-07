$(document).ready(function() {

	function dynamicData() {
		var required_data1 = """ + str(required_data1) + """;

		console.log(required_data1.data[0]['highPrice']);
	    console.log(required_data1)
	    object_length = required_data1['data']['length'];

	    console.log(required_data1.data[1]['highPrice']);
		console.log(required_data1['data'][0]['symbol']);

		// console.log(required_data1);
		console.log("chut chut chut chut");
	}

});