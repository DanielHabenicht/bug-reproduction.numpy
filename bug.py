# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("export.csv", index_col="Timestamp", parse_dates=True)

start = pd.Timestamp("2019-01-15 23:00:00+0000", tz="UTC")
end = pd.Timestamp("2019-02-01 09:50:00+0000", tz="UTC")
print(start)
print(df.index[0])
print(end)

fig, ax = plt.subplots()
ax.axvspan(
    start,  # or df.index[0]
    end,  # or df.index[-1]
    color="red",
    alpha=0.1,
    lw=0,
    zorder=1,
)

# Using the `ax.plot` method works
# ax.plot(df.index, df["n1"], color="black", alpha=0.2, linestyle="solid", zorder=3)

df.plot(ax=ax, alpha=0.2, linestyle="solid", zorder=3)

# Using `axvspan` before and after the plot actually works too
# Only using this axvspan method results in a blank graph
# ax.axvspan(
#     start,
#     end,
#     color="red",
#     alpha=0.1,
#     lw=0,
#     zorder=1,
# )

plt.show()

# %%
