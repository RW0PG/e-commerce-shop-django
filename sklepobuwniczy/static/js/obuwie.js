simpleCart({

			// array representing the format and columns of the cart,
			// see the cart columns documentation
			cartColumns : [ {
				attr : "name",
				label : "Produkt"
			}, {
				view : 'image',
				attr : 'thumb',
				label : false
			}, {
				view : "currency",
				attr : "price",
				label : "Cena"
			}, {
				view : "remove",
				text : '<span class="fas fa-times"></span>',
				label : "Usun"
			} ],

			// "div" or "table" - builds the cart as a
			// table or collection of divs
			cartStyle : "table",

			// how simpleCart should checkout, see the
			// checkout reference for more info
			checkout : {
				type : "SendForm",
				url: "checkout/",
				method: "POST",
				
			},

			// set the currency, see the currency
			// reference for more info
			currency : "PLN",

			// collection of arbitrary data you may want to store
			// with the cart, such as customer info
			data : {},

			// set the cart langauge
			// (may be used for checkout)
			language : "english-us",

			// array of item fields that will not be
			// sent to checkout
			excludeFromCheckout : [],

			// custom function to add shipping cost
			shippingCustom : null,

			// flat rate shipping option
			shippingFlatRate : 15,

			// added shipping based on this value
			// multiplied by the cart quantity
			shippingQuantityRate : 0,

			// added shipping based on this value
			// multiplied by the cart subtotal
			shippingTotalRate : 0,

			// tax rate applied to cart subtotal
			taxRate : 0,

			// true if tax should be applied to shipping
			taxShipping : false,

			// event callbacks
			beforeAdd : null,
			afterAdd : null,
			load : null,
			beforeSave : null,
			afterSave : null,
			update : null,
			ready : null,
			checkoutSuccess : null,
			checkoutFail : null,
			beforeCheckout : null,
			beforeRemove : null
		});
		var licznik0 = 1;
		$('#togglebutt').on('click', function() {
			if (licznik0 % 2 != 0) {
				

				$('#togglebutt').css("background-color", "#ff5a00");
			} else {
				
				$('#togglebutt').css("background-color", "white");
			}
			licznik0++;

		});
		$(window).scroll(function() {
			if ($(window).scrollTop() > 10) {
				$('#navBar').addClass('floatingNav');
			} else {
				$('#navBar').removeClass('floatingNav');
			}
		});

		$('#navbarSupportedContent')
				.on(
						'show.bs.collapse',
						function() {
							document.getElementById("navbarSupportedContent").className = "collapse navbar-collapse text-center collapsednavbarcss1";
							document.getElementById("szukajcss").className = "szukajcss1";
							document.getElementById("szukajform").className = "form-control mr-sm-0 input szukajform1";
							document.getElementById("koszykcss").className = "koszykcss1";
							document.getElementById("logowaniecss").className = "logowaniecss1";
						})

		$('#navbarSupportedContent')
				.on(
						'hide.bs.collapse',
						function() {
							document.getElementById("navbarSupportedContent").className = "collapse navbar-collapse justify-content-start collapsednavbarcss";
							document.getElementById("szukajcss").className = "szukajcss";
							document.getElementById("szukajform").className = "form-control mr-sm-0 input szukajform";
							document.getElementById("koszykcss").className = "koszykcss";
							document.getElementById("logowaniecss").className = "logowaniecss";
						})

		// basic callback example
		simpleCart.bind("afterAdd", function() {
			$(".przyciskkoszyk").fadeOut(400).fadeIn(400);
		});

		simpleCart.bind('update', function() {
			if (simpleCart.quantity() == 0) {
				$(".hideIfEmpty").hide();
				$(".showIfEmpty").show();
			} else {
				$(".hideIfEmpty").show();
				$(".showIfEmpty").hide();
			}
		});
		var licznik1 = 1;

		function myFunc1() {

			if (licznik1 % 2 != 0) {

				document.getElementById("znax1").className = "fas fa-angle-down";
			} else {
				document.getElementById("znax1").className = "fas fa-angle-up";
			}
			licznik1++;

		}

		var licznik2 = 1;

		function myFunc2() {

			if (licznik2 % 2 != 0) {

				document.getElementById("znax2").className = "fas fa-angle-down";
			} else {
				document.getElementById("znax2").className = "fas fa-angle-up";
			}
			licznik2++;

		}

		var licznik3 = 1;

		function myFunc3() {

			if (licznik3 % 2 != 0) {

				document.getElementById("znax3").className = "fas fa-angle-down";
			} else {
				document.getElementById("znax3").className = "fas fa-angle-up";
			}
			licznik3++;

		}
		var container = document.querySelector('[data-ref="container"]');

		var mixer = mixitup(container, {
			callbacks : {
				onMixEnd : function(state) {
					if (state.hasFailed) {
						$("#noItemsFoundMessage").css("display", "block");

					}
					// ## 3 - hasFailed false? hide alert
					else {
						$("#noItemsFoundMessage").css("display", "none");

					}
				}

			},
			animation : {
				duration : 350
			},
			selectors : {
				control : '[data-mixitup-control]'
			}
		});
		var inputSearch = document.querySelector('[data-ref="input-search"]');
		var keyupTimeout;
		// Set up a handler to listen for "keyup" events from the search input
		inputSearch.addEventListener('keyup', function() {
			var searchValue;
			if (inputSearch.value.length < 3) {
				// If the input value is less than 3 characters, don't send
				searchValue = '';
			} else {
				searchValue = inputSearch.value.toLowerCase().trim();
			}
			// Very basic throttling to prevent mixer thrashing. Only search
			// once 350ms has passed since the last keyup event
			clearTimeout(keyupTimeout);
			keyupTimeout = setTimeout(function() {
				filterByString(searchValue);
			}, 350);
		});

		/**
		 * Filters the mixer using a provided search string, which is matched against
		 * the contents of each target's "class" attribute. Any custom data-attribute(s)
		 * could also be used.
		 *
		 * @param  {string} searchValue
		 * @return {void}
		 */
		function filterByString(searchValue) {
			if (searchValue) {
				// Use an attribute wildcard selector to check for matches
				mixer.filter('[class*="' + searchValue + '"]');
			} else {
				// If no searchValue, treat as filter('all')
				mixer.filter('all');
			}
		}
		
		function fn1() {
			simpleCart.update();
			simpleCart.empty();
			simpleCart.update();
		}
		
		//export { simpleCart };

		/*  var noItemsFoundMessage = document.getElementById("noItemsFoundMessage");
		noItemsFoundMessage.style.display = "none";

		//  MIXITUP 3 plugin settings
		    mixitup(container, {   
		          // ## 2 - callbacks onMixEnd 
		         callbacks: {
		         onMixEnd: function(state){
		           // ## 3 - hasFailed true? show alert
		           if(state.hasFailed){  
		              noItemsFoundMessage.style.display = "block";
		              alert("No items found");
		           }
		           // ## 3 - hasFailed false? hide alert
		           else{
		              noItemsFoundMessage.style.display = "none";
		              alert("Items found");
		           }
		         },
		      
		      }  */