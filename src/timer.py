import asyncio


class Timer:
  def __init__(self, callback):
    self._task = asyncio.ensure_future(self._job())
    self._timeout =  60 * 2 # 2 minutes
    self._callback = callback
  
  async def _job(self):
    while True:
      await asyncio.sleep(self._timeout)
      await self._callback()

