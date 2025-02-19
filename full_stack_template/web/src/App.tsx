import { Loader2 } from "lucide-react"
import { Card } from "./components/ui/card"
import { options, useQuery } from "./hooks/fetcher"

function App() {
  const { data, error, isLoading } = useQuery(
    "/api/status/", undefined, options
  );

  return (
    <main className="flex min-h-screen items-center justify-center p-5">
      <Card className="p-6">
        {isLoading ? (
          <Loader2 className="animate-spin h-6 w-6" />
        ) : error ? (
          <div className="text-destructive">Error: {error.message}</div>
        ) : (
          <div className="text-xl">
            API Status: {data?.status || 'Unknown'}
          </div>
        )}
      </Card>
    </main>
  )
}

export default App
