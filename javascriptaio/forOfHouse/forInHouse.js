const house = {
	sqft: 800,
	bedrooms: 2,
	bathrooms: 1,
};

let houseDetails = '<h2>Information about this house </hs>';

for (let prop in house) {
	houseDetails = `${houseDetails}<br>${prop}:${house[prop]}<br>`;
	document.getElementById('root').innerHTML = houseDetails;
}
