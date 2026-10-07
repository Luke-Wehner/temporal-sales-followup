# Temporal Sales Follow-Up Workflow

A simple sales follow-up workflow built with Temporal's Python SDK to explore durable execution through a real-world sales use case.

## Why I Built This

I'm a sales professional, not a software engineer. I built this project while learning more about Temporal because I wanted to understand the product beyond the sales and marketing language.

Sales follow-up is a simple example of a long-running business process: an action happens, time passes, and another action needs to occur reliably later. In a real sales organization, those waits could last days or weeks and involve multiple steps.

Temporal's durable execution model makes that concept particularly interesting because the workflow's state and progress don't have to depend on a single continuously running application process.

## What the Demo Does

The workflow:

1. Starts a follow-up process for a prospect.
2. Uses a Temporal durable timer to wait.
3. Automatically resumes after the timer.
4. Returns the next sales follow-up action.

For demonstration purposes, the timer is 10 seconds rather than several days.

Example output:

`Follow up with Acme Corp: send the next personalized sales touchpoint.`

## What I Used

- Temporal
- Temporal Python SDK
- Python
- Temporal CLI
- Temporal Web UI
- GitHub

## What I Learned

Building the workflow helped me better understand the distinction between simply executing code and reliably executing a business process over time.

Even in this small example, the workflow logic can describe what should happen next while Temporal handles the execution state and durable waiting underneath it.

For a production sales workflow, the same concept could be extended to CRM updates, email activities, reply signals, task creation, approval steps, and longer follow-up sequences.

## Project Structure

- `workflow.py` — defines the sales follow-up workflow and durable timer
- `worker.py` — runs the Temporal worker
- `start_workflow.py` — starts the demo workflow
- `requirements.txt` — Python dependency
