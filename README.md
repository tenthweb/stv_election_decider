# Election Simulator

This program allows users to quickly set up and run a simulated election using the **Single Transferable Vote (STV)** system. The tool is designed for experimentation, learning, and testing election logic rather than for real-world vote collection.

## Features

Using simple prompts, the program lets you define:

- A list of candidate names (entered as comma-separated values)
- The number of seats to be filled
- The number of ballots to generate

From these inputs, the program generates a complete election dataset, including ranked ballots, is then passed directly into the STV counting engine. The simulator supports fractional vote transfers, a Droop quota, and round-by-round reporting, making the full counting process transparent and easy to follow.

## Intended Use

This program is intended to be:

- Easy to use for non-technical users
- Suitable for simulations demonstrations, coursework