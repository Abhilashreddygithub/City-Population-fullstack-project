export async function getCity(name) {
  const res = await fetch(`/api/city/${name}`);
  return res.json();
}
