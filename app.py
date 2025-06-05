from fastapi import FastAPI, Response
import matplotlib.pyplot as plt
import io

app = FastAPI()

@app.get("/plot")
def get_plot():
    # Create a simple plot
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.title("Simple Line Plot")

    # Save plot to a bytes buffer instead of file
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    # Return image as response
    return Response(content=buf.getvalue(), media_type="image/png")
