from unittest import TestCase
from unittest.async_case import IsolatedAsyncioTestCase

from common_data import session


class TestStudentTranscriptGetter(TestCase):
    def test_handler(self):
        """测试获取学生成绩"""
        from xtu_ems.ems.handler.get_students_transcript import StudentTranscriptGetter
        handler = StudentTranscriptGetter()
        resp = handler.handler(session)
        print(resp.model_dump_json(indent=4))
        self.assertIsNotNone(resp)


class TestAsyncStudentTranscriptGetter(IsolatedAsyncioTestCase):
    async def test_async_handler(self):
        """测试异步获取学生成绩"""
        from xtu_ems.ems.handler.get_students_transcript import StudentTranscriptGetter
        handler = StudentTranscriptGetter()
        resp = await handler.async_handler(session)
        print(resp.model_dump_json(indent=4))
        self.assertIsNotNone(resp)


class TestStudentRankGetter(TestCase):
    def test_handler(self):
        """测试获取学生排名"""
        from xtu_ems.ems.handler.get_students_transcript import StudentRankGetter
        handler = StudentRankGetter()
        resp = handler.handler(session)
        print(resp.model_dump_json(indent=4))
        self.assertIsNotNone(resp)


class TestAsyncStudentRankGetter(IsolatedAsyncioTestCase):
    async def test_async_handler(self):
        """测试异步获取学生排名"""
        from xtu_ems.ems.handler.get_students_transcript import StudentRankGetter
        handler = StudentRankGetter()
        resp = await handler.async_handler(session)
        print(resp.model_dump_json(indent=4))
        self.assertIsNotNone(resp)
