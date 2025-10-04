import meep as mp
print(mp.__version__)
cell_size = mp.Vector3(10, 10)
geometry = [mp.Block(size=mp.Vector3(2, 1, 1), center=mp.Vector3(), material=mp.Medium(epsilon=12))]
sources = [mp.Source(src=mp.ContinuousSource(frequency=1), component=mp.Ez, center=mp.Vector3(-4, 0))]
sim = mp.Simulation(cell_size=cell_size, geometry=geometry, sources=sources, boundary_layers=[mp.PML(0.5)])
sim.run(until=100)
print("FDTD Simulation Ran Successfully!")
