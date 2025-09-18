import React from 'react';

export default function CityTable({ cities = [] }) {
	if (!cities || cities.length === 0) {
		return <p>No cities available</p>;
	}

	return (
		<table>
			<thead>
				<tr>
					<th>Name</th>
					<th>Population</th>
				</tr>
			</thead>
			<tbody>
				{cities.map((c) => (
					<tr key={c.name}>
						<td>{c.name}</td>
						<td>{c.population}</td>
					</tr>
				))}
			</tbody>
		</table>
	);
}
