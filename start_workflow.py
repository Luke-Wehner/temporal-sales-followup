import asyncio

from temporalio.client import Client

from workflow import SalesFollowUpWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        SalesFollowUpWorkflow.run,
        "Acme Corp",
        id="sales-followup-acme",
        task_queue="sales-followup",
    )

    print("Workflow completed!")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
