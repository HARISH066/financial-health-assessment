function Dashboard({ data }) {
  return (
    <div>
      <h3>Metrics</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default Dashboard;
