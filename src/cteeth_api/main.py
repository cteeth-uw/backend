
import argparse
import uvicorn

from cteeth_api.app import CTeethApp


def main():
    parser = argparse.ArgumentParser(description="CTeeth API Server")
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Address to listen on"
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to listen on"
    )
    parser.add_argument(
        "--reload", dest="reload", action="store_true", default=True, help="Enable auto-reload for development purposes"
    )
    parser.add_argument(
        "--no-reload", dest="reload", action="store_false", help="Disable auto-reload for development purposes"
    )
    args = parser.parse_args()
    
    # Placeholder for future functionality
    print(f"CTeeth API is running on {args.host}:{args.port}. Reload enabled: {args.reload}. Use --help for more options.")

    uvicorn.run("cteeth_api.app:app", host=args.host, port=args.port, reload=args.reload)


if __name__ == "__main__":
    main()
