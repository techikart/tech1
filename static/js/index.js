window.onload = function(){
	//cart box
	const iconShopping = document.querySelector('.iconShopping');
	const cartCloseBtn = document.querySelector('.fa-close');
	const cartBox = document.querySelector('.cartBox');
	iconShopping.addEventListener("click",function(){
		cartBox.classList.add('active');
	});
	cartCloseBtn.addEventListener("click",function(){
		cartBox.classList.remove('active');
	});



	// localstorage basics
	if(typeof(Storage) !== 'undefined'){
		// const array = ['a','b','c','d'];
		// const object = [

		// 				{

		// 					name:'Raman Sharma',
		// 					channelName: 'Fullyworld web tutorials',
		// 					address:{
		// 						houseNo:'252'
		// 					}
		// 				},
		// 				{

		// 					name:'Raman Sharma 2',
		// 					channelName: 'Fullyworld web tutorials',
		// 					address:{
		// 						houseNo:'252'
		// 					}
		// 				},

		// 			];
		// localStorage.setItem("localstoragedemotut",JSON.stringify(object));
		// localStorage.setItem("localstoragedemotut",array);
		// localStorage.setItem("localstoragedemotut",45);


		//get data from local storage

		// const data = localStorage.getItem("localstoragedemotut");
		// console.log(JSON.parse(data)[0].channelName);

		// console.log(data[3]);
		// console.log(data);

		// localStorage.removeItem("localstoragedemotut");
	}else{
		console.log('storage is not working on your browser');
	}
}