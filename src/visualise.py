import matplotlib.pyplot as plt
import pandas as pd

def plot_trend_volatility(df: pd.DataFrame) -> None:
    ticker = df.columns[0]
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))
    axes[0].plot(df[ticker], 'b-', label="Daily")
    axes[1].plot(df[ticker].rolling(21).mean(), 'g-', label="Trend (21-day MA)")
    axes[2].plot(df[ticker].rolling(21).std(), 'r-', label="21-day Volatility")
    for ax in axes:
        ax.grid(alpha=0.7)
        ax.legend()
    plt.suptitle(f"{ticker} Price Trend & Volatility Analysis")
    plt.tight_layout()
    plt.savefig(f"outputs/{ticker}_trend_volatility.png")
    #plt.show()

def plot_returns(df: pd.DataFrame) -> None:
    ticker = df.columns[0]
    fig, axes = plt.subplots(4, 1, figsize=(12, 8))
    axes[0].plot(df[ticker].pct_change(1), 'b-', label="Daily Return", alpha=0.5)
    axes[1].plot(df[ticker].resample("W").last().pct_change(), 'b-', label="Weekly Return", alpha=0.5)
    axes[2].plot(df[ticker].resample("ME").last().pct_change(), 'ro-', label="Monthly Return")
    axes[3].plot(df[ticker].resample("YE").last().pct_change(), 'gs-', label="Annual Return")
    for ax in axes:
        ax.grid(alpha=0.7)
        ax.legend()
    plt.suptitle(f"{ticker} Returns Across Different Time Horizons")
    plt.tight_layout()
    plt.savefig(f"outputs/{ticker}_returns.png")
    #plt.show()

def plot_cumulative_return(df: pd.DataFrame) -> None:
    ticker = df.columns[0]
    cumulative_return = df[ticker].pct_change().add(1).cumprod().sub(1).mul(100)
    plt.figure(figsize=(12, 5))
    plt.plot(cumulative_return, 'b-', linewidth=2, label=f"{ticker} Cumulative Return")
    plt.axhline(0, linestyle='--', color='black', alpha=0.3)
    plt.legend()
    plt.grid(alpha=0.7)
    plt.title(f"{ticker} Cumulative Return (%)")
    plt.tight_layout()
    plt.savefig(f"outputs/{ticker}_cumulative_return.png")
    #plt.show()

def plot_price_analysis(df: pd.DataFrame) -> None:
    ticker = df.columns[0]
    returns = df[ticker].pct_change()
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))
    axes[0].plot(df[ticker],'b-')
    axes[0].set_title(f"{ticker} Price")
    axes[1].plot(returns,'g-')
    axes[1].set_title("Daily Returns")
    axes[2].hist(returns.dropna(), bins=50)
    axes[2].set_title("Returns Distribution")
    for ax in axes:
        ax.grid(alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"outputs/{ticker}_price_analysis.png")
    #plt.show()