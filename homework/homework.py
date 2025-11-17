# Cargue los datos de la tabla "files/input/drivers.csv" y "files/input/timesheet.csv""
# a una variable llamada drivers y timesheet
import pandas as pd
drivers = pd.read_csv("files/input/drivers.csv")
timesheet = pd.read_csv("files/input/timesheet.csv")

# Calcule el promedio de las columnas "hours-logged" y "miles-logged"
avg_timesheet = timesheet.groupby("driverId")["hours-logged"].mean().reset_index()
avg_timesheet.rename(columns={"hours-logged": "mean_hours-logged"}, inplace=True)

# Cree una tabla llamada "timesheet_below" a partir de "timesheet"
# donde "hours-logged" sea menor que "mean_hours-logged"
timesheet_with_means = pd.merge(timesheet_with_means, avg_timesheet, on="driverId", how="left")
timesheet_below = timesheet_with_means[timesheet_with_means["hours-logged"] < timesheet_with_means["mean_hours-logged"]]

#

sum_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].sum().reset_index()

min_max_timesheet = timesheet.groupby("driverId")["hours-logged"].agg(["min", "max"]).reset_index()

summary = pd.merge(sum_timesheet, drivers[["driverId", "name"]], on="driverId", how="left")

summary.to_csv("files/output/summary.csv", index=False)

top10 = summary.sort_values(by="miles-logged", ascending=False).head(10)

plt.figure(figsize=(8, 5))
plt.barh(top10["name"], top10["miles-logged"], color="lightblue")
plt.xlabel("Millas registradas")
plt.ylabel("Conductor")
plt.title("Top 10 conductores por millas registradas")
plt.gca().invert_yaxis()  # El conductor con más millas arriba
plt.tight_layout()

plt.savefig("files/plots/top10_drivers.png")
plt.close()

print("Archivos generados correctamente:")
print(" - files/output/summary.csv")
print(" - files/plots/top10_drivers.png")