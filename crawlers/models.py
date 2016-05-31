from __future__ import unicode_literals

from django.conf import settings
import redis
import json


class Job(object):
    """ Base class for job """

    def get_redis_conn(self):
        return redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
            db=settings.REDIS_DB
        )


    def break_down(self):
        """
        """
        raise NotImplementedError

    def distribute(self, redis_conn=None):
        " push jobs to Redis "

        jobs = self.break_down()
        redis_conn = redis_conn or self.get_redis_conn()
        redis_conn.rpush('task_queue', *jobs)
        print 'Distributed %d jobs into Redis' % len(jobs)


class ASICJob(Job):

    def break_down(self):
        """
        break down the job and returns a deque object of smaller chunks
        """

        project = 'DOSWebCrawler'
        spider = 'asic'
        start_index = 200000
        end_index = 500000
        step = 100

        registers = (
            'Australian Financial Services Licensee',
            'Australian Financial Services Authorised Representative',
            'Credit Representative',
            'Credit Licensee'
        )
        jobs = []
        for register in registers:
            for index in xrange(start_index, end_index, step):
                job = {
                    'project': project,
                    'spider': spider,
                    'register': register,
                    'start_index': index,
                    'end_index': index + step
                }
                jobs.append(json.dumps(job))
        return jobs


class JPCrawlingJob(Job):

    def break_down(self):
        """
        break down the job and returns a deque object of smaller chunks
        """

        project = 'DOSWebCrawler'
        spider_names = [
            'act',
            'nsw',
            'nt',
            'qld',
            'sa',
            'vic',
            'wa',
        ]
        jobs = []
        for spider in spider_names:
            job = {
                'project': project,
                'spider': spider,
            }
            jobs.append(json.dumps(job))

        return jobs